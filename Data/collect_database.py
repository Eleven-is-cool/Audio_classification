# classes = ['air_conditioner', 'car_horn', 'children_playing', 'dog_bark', 'drilling', 'engine_idling', 'gun_shot', 'jackhammer', 'siren', 'street_music']
import os
import csv
from shutil import copyfile

# 文件路径
def file_path(root):
    data_oldPath = os.path.join(root, 'UrbanSound8K')
    csv_file = os.path.join(data_oldPath, 'metadata/UrbanSound8K.csv')
    audio_oldPath = os.path.join(data_oldPath, 'audio')
    return csv_file, audio_oldPath


# 从csv文件中计算总共文件数量
def countrows(csv_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        totalRows = len(rows)
        return totalRows


# 创建新的路径
def mkdir_new_path(root, new_dir_name):
    audio_newPath = os.path.join(root, new_dir_name)
    if not os.path.isdir(audio_newPath):
        os.mkdir(audio_newPath)
    return audio_newPath


# 复制音频文件到新的路径中
def copytonewpath(csv_file, audio_oldPath, audio_newPath, totalRows):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        currentNumber = 1
        for row in reader:
            src = os.path.join(audio_oldPath, 'fold' + row['fold'], row['slice_file_name'])
            # 将原数据集分成两个文件夹children_playing和others
            if row['class'] == 'children_playing':
                dst_fold = os.path.join(audio_newPath, 'children_playing')
            else:
                dst_fold = os.path.join(audio_newPath, 'others')
            dst = os.path.join(dst_fold, row['slice_file_name'])
            print('copying ', currentNumber, '/', totalRows, row['slice_file_name'], 'to', dst_fold)
            if not os.path.isdir(dst_fold):
                os.mkdir(dst_fold)
            if os.path.isfile(src):
                copyfile(src, dst)
            currentNumber += 1


if __name__ == '__main__':
    # 原文件路径
    root = 'F:\code\Audio_classification\dataBase'
    csv_file, audio_oldPath = file_path(root)
    # print('csv_file =', os.path.isfile(csv_file), csv_file)
    # print('audio =', os.path.isdir(audio_in), audio_in)
    totalRows = countrows(csv_file)
    new_dir_name = 'UrbanSound8K_byclass'
    audio_newPath = mkdir_new_path(root, new_dir_name)
    copytonewpath(csv_file, audio_oldPath, audio_newPath, totalRows)





