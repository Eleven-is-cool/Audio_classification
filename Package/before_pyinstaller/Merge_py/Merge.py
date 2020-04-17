import os
import sys
from pydub import AudioSegment


def Merge(result, desti):
    path = "temp"
    list = []
    i = 0
    for filename in os.listdir(path):
        if result[i] == 'person':
            list.append(AudioSegment.from_wav(path+"/"+filename))
        i=i+1
    count=len(list)

    # 输出音频文件
    output_music=list[0]
    for j in range(1,count):
        output_music=output_music+list[j]
    output_music.export(desti, format="wav")


if __name__ == '__main__':
    # s = "person person person person person person person person person"
    # 将字符串转化成数组
    # sys[1]-分类列表，sys[2]-合并结果路径，包括新音频命名
    Merge(sys.argv[1].split(), sys.argv[2])



