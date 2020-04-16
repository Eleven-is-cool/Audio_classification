import os

from pydub import AudioSegment

def Merge(path,result):
    list=[]
    i=0
    for filename in os.listdir(path):
        if(result[i]=='person'):
            list.append(AudioSegment.from_wav(path+"/"+filename))
        i=i+1
    count=len(list)

    #输出音频文件
    output_music=list[0]
    for j in range(1,count):
        output_music=output_music+list[j]
    output_music.export("D:/AudioRecognition/he.wav", format="wav")

if __name__ == '__main__':
    #获取的列表
    result=['person','others','person','person','other','other','other','person','person','other']
    #需要合成音频的文件夹
    path="D:\AudioRecognition\qiefen"
    Merge(path,result)



