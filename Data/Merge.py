import os

from pydub import AudioSegment

def Merge(path):
    #需要合成的音频文件计数
    count=0
    for filename in os.listdir(path):
        count=count+1

    list=[]
    i=1
    for j in range(count):
        list.append("input_music"+str(i))
        i=i+1
    j=0
    for filename in os.listdir(path):
        list[j]=AudioSegment.from_wav(path+"/"+filename)
        j=j+1
    #输出音频文件
    output_music=list[0]
    for j in range(1,count):
        output_music=output_music+list[j]
    output_music.export("D:/AudioRecognition/he.wav", format="wav")

if __name__ == '__main__':
    #需要合成音频的文件夹
    path="D:/AudioRecognition/hebing"
    Merge(path)



