import os
from pydub import AudioSegment

oldPath = 'F:\code\Audio_classification\dataBase\zh-CN\clips'
for fileNames in os.walk(oldPath):
    for fileName in fileNames[2]:
        name = fileName[1:-4]
        # 把文件名开头第一个c补上，\结尾的字符串拼接不了
        source_file_path = 'F:\code\Audio_classification\dataBase\zh-CN\clips\c' + name + '.mp3'
        destin_path = r'F:\code\Audio_classification\dataBase\zh-CN\UrbanSound8K_byclass\children_playing\c' + name + '.wav'
        sound = AudioSegment.from_mp3(source_file_path)
        sound.export(destin_path, format='wav')
        print(destin_path+"is converting")