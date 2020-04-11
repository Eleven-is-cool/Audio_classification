import os
import wave
from pydub import AudioSegment
import numpy as np
from keras.models import load_model
import librosa


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


def main():
    path = "highMass/highMass.wav"
    res = []
    model = load_model('model0404.h5')
    cut(path)# 将文件切割完放入temp文件夹
    for fileNames in os.walk("temp/"):
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
    return res


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


# 切割
def cut(main_wav_path):
    time = getTime(main_wav_path)
    # 换算成毫秒
    mstime = time * 1000
    begin = 0
    end = int(time) * 1000
    # 循环切割
    while begin <= end:
        # 保存出来的目的路径
        part_wav_path = "temp/temp"+str(begin)+".wav"
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


