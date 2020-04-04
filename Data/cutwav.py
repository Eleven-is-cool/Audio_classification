import wave
from pydub import AudioSegment

# 获得时间
def getTime(wav_path):
    with wave.open(wav_path, "rb") as f:
        f = wave.open(wav_path)
        # print(f.getparams())
        rate = f.getframerate()
        frames = f.getnframes()
        duration = frames / float(rate)
        print(duration)
        print(int(duration))
        return duration


# 根据参数切割音频
def getEachWav(main_wav_path, start_time, end_time, part_wav_path):
    start_time = int(start_time)
    end_time = int(end_time)
    # sound = AudioSegment.from_mp3(main_wav_path)
    sound = AudioSegment.from_wav(main_wav_path)
    word = sound[start_time:end_time]
    word.export(part_wav_path, format="wav")


if __name__ == '__main__':

    main_wav_path = r"C:\Users\Eleven\Desktop\nothing.wav"
    time = getTime(main_wav_path)
    # 换算成毫秒
    mstime = time * 1000
    begin = 0
    end = int(time) * 1000
    # 循环切割
    while begin <= end:
        # 保存出来的目的路径
        part_wav_path = "F:/code/Audio_classification/dataBase/UrbanSound8K_byclass/others/nothing"+str(begin)+".wav"
        # 因为是一秒一秒的分，为了得到完整的音频，即7.2s这种情况，加到7s的时候，要将剩下的200ms也取出来，所以在这里分开讨论
        if begin == end:
            start_time = begin
            end_time = mstime
            getEachWav(main_wav_path, start_time, end_time, part_wav_path)
            print(str(start_time) + " is successful")
        else:
            start_time = begin
            end_time = begin+2000
            getEachWav(main_wav_path, start_time, end_time, part_wav_path)
            print(str(start_time) + " is successful")

        begin += 2000
