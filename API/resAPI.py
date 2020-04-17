from pydub import AudioSegment
from keras.models import load_model
import librosa
import flask
import numpy as np
import wave
import nextpow2
import math
import shutil
import os

app = flask.Flask(__name__)


@app.route('/predict', methods=["GET", "POST"])
def getRes():
    data = {"success": False}
    params = flask.request.json
    if (params == None):
        params = flask.request.args
    if (params != None):
        path = params.get("msg")
        Enhance_speach("./file/"+path)
        main("./highMass/highMass.wav")# 将文件切割完放入temp文件夹
        res = []
        for fileNames in os.walk("./temp"):
            for fileName in fileNames[2]:
                File = os.path.join(fileNames[0], fileName)
                wavs = []
                wavs.append(wav2mfcc(File, 11))
                X = np.array(wavs)
                X = X.reshape(-1, 220)
                result = model.predict(X[0:1])[0]
                name = ["others", "person"]
                ind = 0
                for i in range(len(result)):
                    if result[i] > result[ind]:
                        ind = 1
                res.append(name[ind])
        data["prediction"] = res
        data["success"] = True
    clean()
    return flask.jsonify(data)


def Enhance_speach(path):
    # 打开WAV文档
    f = wave.open(path)
    # 读取格式信息
    # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    fs = framerate
    # 读取波形数据
    str_data = f.readframes(nframes)
    f.close()
    # 将波形数据转换为数组
    x = np.fromstring(str_data, dtype=np.short)
    # 计算参数
    len_ = 20 * fs // 1000 # 样本中帧的大小
    PERC = 50 # 窗口重叠占帧的百分比
    len1 = len_ * PERC // 100  # 重叠窗口
    len2 = len_ - len1   # 非重叠窗口
    # 设置默认参数
    Thres = 3
    Expnt = 2.0
    beta = 0.002
    G = 0.9
    # 初始化汉明窗
    win = np.hamming(len_)
    # normalization gain for overlap+add with 50% overlap
    winGain = len2 / sum(win)

    # Noise magnitude calculations - assuming that the first 5 frames is noise/silence
    nFFT = 2 * 2 ** (nextpow2.nextpow2(len_))
    noise_mean = np.zeros(nFFT)

    j = 0
    for k in range(1, 6):
        noise_mean = noise_mean + abs(np.fft.fft(win * x[j:j + len_], nFFT))
        j = j + len_
    noise_mu = noise_mean / 5

    # --- allocate memory and initialize various variables
    k = 1
    img = 1j
    x_old = np.zeros(len1)
    Nframes = len(x) // len2 - 1
    xfinal = np.zeros(Nframes * len2)

    # =========================    Start Processing   ===============================
    for n in range(0, Nframes):
        # Windowing
        insign = win * x[k-1:k + len_ - 1]
        # compute fourier transform of a frame
        spec = np.fft.fft(insign, nFFT)
        # compute the magnitude
        sig = abs(spec)

        # save the noisy phase information
        theta = np.angle(spec)
        SNRseg = 10 * np.log10(np.linalg.norm(sig, 2) ** 2 / np.linalg.norm(noise_mu, 2) ** 2)


        def berouti(SNR):
            if -5.0 <= SNR <= 20.0:
                a = 4 - SNR * 3 / 20
            else:
                if SNR < -5.0:
                    a = 5
                if SNR > 20:
                    a = 1
            return a


        def berouti1(SNR):
            if -5.0 <= SNR <= 20.0:
                a = 3 - SNR * 2 / 20
            else:
                if SNR < -5.0:
                    a = 4
                if SNR > 20:
                    a = 1
            return a

        if Expnt == 1.0:  # 幅度谱
            alpha = berouti1(SNRseg)
        else:  # 功率谱
            alpha = berouti(SNRseg)
        #############
        sub_speech = sig ** Expnt - alpha * noise_mu ** Expnt;
        # 当纯净信号小于噪声信号的功率时
        diffw = sub_speech - beta * noise_mu ** Expnt
        # beta negative components

        def find_index(x_list):
            index_list = []
            for i in range(len(x_list)):
                if x_list[i] < 0:
                    index_list.append(i)
            return index_list

        z = find_index(diffw)
        if len(z) > 0:
            # 用估计出来的噪声信号表示下限值
            sub_speech[z] = beta * noise_mu[z] ** Expnt
            # --- implement a simple VAD detector --------------
        if SNRseg < Thres:  # Update noise spectrum
            noise_temp = G * noise_mu ** Expnt + (1 - G) * sig ** Expnt  # 平滑处理噪声功率谱
            noise_mu = noise_temp ** (1 / Expnt)  # 新的噪声幅度谱
        # flipud函数实现矩阵的上下翻转，是以矩阵的“水平中线”为对称轴
        # 交换上下对称元素
        sub_speech[nFFT // 2 + 1:nFFT] = np.flipud(sub_speech[1:nFFT // 2])
        x_phase = (sub_speech ** (1 / Expnt)) * (np.array([math.cos(x) for x in theta]) + img * (np.array([math.sin(x) for x in theta])))
        # take the IFFT

        xi = np.fft.ifft(x_phase).real
        # --- Overlap and add ---------------
        xfinal[k-1:k + len2 - 1] = x_old + xi[0:len1]
        x_old = xi[0 + len1:len_]
        k = k + len2
    # 保存文件
    wf = wave.open('./highMass/highMass.wav', 'wb')
    # 设置参数
    wf.setparams(params)
    # 设置波形文件 .tostring()将array转换为data
    wave_data = (winGain * xfinal).astype(np.short)
    wf.writeframes(wave_data.tostring())
    wf.close()


def wav2mfcc(path, max_pad_size=11):
    y, sr = librosa.load(path=path, sr=None, mono=1)
    y = y[::3]
    audio_mac = librosa.feature.mfcc(y=y, sr=16000)
    y_shape = audio_mac.shape[1]
    if y_shape < max_pad_size:
        pad_size = max_pad_size - y_shape
        audio_mac = np.pad(audio_mac, ((0, 0), (0, pad_size)), mode='constant')
    else:
        audio_mac = audio_mac[:, :max_pad_size]
    return audio_mac

# 获得时间
def getTime(wav_path):
    with wave.open(wav_path, "rb") as f:
        f = wave.open(wav_path)
        # print(f.getparams())
        rate = f.getframerate()
        frames = f.getnframes()
        duration = frames / float(rate)
        # print(duration)
        # print(int(duration))
        return duration


# 根据参数切割音频
def getEachWav(main_wav_path, start_time, end_time, part_wav_path):
    start_time = int(start_time)
    end_time = int(end_time)
    # sound = AudioSegment.from_mp3(main_wav_path)
    sound = AudioSegment.from_wav(main_wav_path)
    word = sound[start_time:end_time]
    word.export(part_wav_path, format="wav")


def main(main_wav_path):
    time = getTime(main_wav_path)
    # 换算成毫秒
    mstime = time * 1000
    begin = 0
    end = int(time) * 1000
    # 循环切割
    while begin <= end:
        # 保存出来的目的路径
        part_wav_path = "./temp/temp"+str(begin)+".wav"
        # 因为是一秒一秒的分，为了得到完整的音频，即7.2s这种情况，加到7s的时候，要将剩下的200ms也取出来，所以在这里分开讨论
        if begin == end:
            start_time = begin
            end_time = mstime
            getEachWav(main_wav_path, start_time, end_time, part_wav_path)

        else:
            start_time = begin
            end_time = begin+1000
            getEachWav(main_wav_path, start_time, end_time, part_wav_path)

        begin += 1000


def clean():
    shutil.rmtree('./highMass')
    os.mkdir('./highMass')
    shutil.rmtree('./temp')
    os.mkdir('./temp')


if __name__ == '__main__':
    model = load_model('model0404.h5')
    print("load model successful")
    app.run("0.0.0.0")
