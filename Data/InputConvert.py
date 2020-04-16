import shutil
from pydub import AudioSegment

def convert(path):
    pic = path.split("\\")[-1]
    if pic.endswith(".mp3"):
        output_music=AudioSegment.from_mp3(path)
        output_music.export("D:\\AudioRecognition\\convert\\convert.wav", format="wav")
    elif pic.endswith(".ogg"):
        output_music=AudioSegment.from_ogg(path)
        output_music.export("D:\\AudioRecognition\\convert\\convert.wav", format="wav")
    elif pic.endswith(".wav"):
        shutil.move(path, "D:\\AudioRecognition\\convert\\convert.wav")


if __name__ == '__main__':
    #导入的音频文件路径
    path = "D:\\AudioRecognition\\ogg.ogg"
    convert(path)