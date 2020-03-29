import wave
import numpy as np
import os
from keras.models import load_model
from keras.models import model_from_json

import librosa

import yaml
from keras.models import model_from_yaml



# 提取 mfcc 参数
def wav2mfcc(path, max_pad_size=11):
  y, sr = librosa.load(path=path, sr=None, mono=1)
  y = y[::3]  #每三个点选用一个
  audio_mac = librosa.feature.mfcc(y=y, sr=16000)
  y_shape = audio_mac.shape[1]
  if y_shape < max_pad_size:
      pad_size = max_pad_size - y_shape
      audio_mac = np.pad(audio_mac, ((0, 0), (0, pad_size)), mode='constant')
  else:
      audio_mac = audio_mac[:, :max_pad_size]
  return audio_mac


if __name__ == '__main__':
    # 加载模型结构
    # model = model_from_yaml(open('F:/code/Audio_classification/Data/architecture.yaml').read())
    # 加载模型参数
    # model.load_weights(r'‪F:/code/Audio_classification/Data/model_weights.h5')
    # 构建模型
    model = load_model('F:/model.h5')# 加载训练模型

    model.summary()
    wavs = []
    print("open module successful")
    wavs.append(wav2mfcc(r"F:\code\Audio_classification\dataBase\UrbanSound8K_byclass\others\4912-3-3-0.wav", 11))
    X=np.array(wavs)
    X= X.reshape(-1, 220)
    print(X.shape)
    result = model.predict(X[0:1])[0]
    print("识别结果", result)
    #  因为在训练的时候，标签集的名字 为：  0：seven   1：stop    0 和 1 是下标
    name = ["others", "person"] # 创建一个跟训练时一样的标签集
    ind = 0 # 结果中最大的一个数
    for i in range(len(result)):
        if result[i] > result[ind]:
            ind = 1
    print("识别的语音结果是：", name[ind])


