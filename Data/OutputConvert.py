import shutil
from pydub import AudioSegment

def convert(path,format):
    pic = path.split("\\")[-1]
    if (format=="mp3"):
        output_music=AudioSegment.from_wav(path)
        output_music.export("D:\\AudioRecognition\\output\\output.mp3", format="mp3")
    elif (format=="ogg"):
        output_music=AudioSegment.from_wav(path)
        output_music.export("D:\\AudioRecognition\\output\\output.ogg", format="ogg")
    elif (format=="wav"):
        shutil.move(path, "D:\\AudioRecognition\\output\\output.wav")


if __name__ == '__main__':
    #导出的音频文件路径
    path = "D:\\AudioRecognition\\test.wav"
    #用户选择导出的格式
    format="wav"
    convert(path,format)