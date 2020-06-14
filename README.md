# Audio_classification
The project is to classify audio

## 数据集
[数据集](https://pan.bnuz.edu.cn/l/b1kxKb)
训练集来自urbanSound8k数据集，清华大学thchs-30普通话语音，Audacity生成的音频，csdn上有关环境的音频与自己录制的音频，最终数据集大小为10G左右，人声和其他声音的音频占比一致。
需要对数据集音频进行切割，转化为统一采样率。
分割音频。[核心代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/cutwav.py)
> librosa库请使用版本不要过高，本次训练用的librosa版本是0.6.0 

## 模型训练
对数据集音频进行降噪，提取mcff系数（梅尔频率倒谱系数），用keras训练出二分类模型
1. 音频降噪。  [代码](https://github.com/Eleven-is-cool/Audio_classification/tree/master/Enhance_speach)
2. 利用Keras训练模型。[训练代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/train.py)
3. 保存模型。[模型下载](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/model.h5)
4. 模型预测。[预测代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/test.py)

## 打包
1. 将目前实现的模块打包。 [Package文件夹](https://github.com/Eleven-is-cool/Audio_classification/tree/master/Package) 
2. 实现web api，可以部署到服务器，但是识别前得先要把 [文件上传](https://github.com/Eleven-is-cool/Audio_classification/blob/master/API/uploadFile.py) 到服务器，这也就导致了只能应用于识别短时音频。[API](https://github.com/Eleven-is-cool/Audio_classification/tree/master/API)
