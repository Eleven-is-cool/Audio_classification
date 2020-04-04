# Audio_classification
The project is to classify audio

## 2020.3.23
对urbanSound的数据集进行分类，暂时分成有语音和无语音的两类

[urbanSound8k原数据集,提取码：b8io ](https://pan.baidu.com/s/1PtomzQCCRcb9CzCjT3ZIeg)

[urbanSound8k整理代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/collect_database.py)

## 2020.3.27

1. 普通话发音音频文件，共19,468个mp3音频文件。[数据集链接,提取码：p0fs](https://pan.baidu.com/s/1HsPmTWw0riPrpBbqdrJDzg)

2. 将上述mp3文件转化成mav文件，并放入urbanSound分类后文件中的语音文件夹。

   [code](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/convertToWav.py)

3. 最终整合后的音频文件分为两类：others和person。

4. 初步训练

   librosa库请使用版本不要过高，本次训练用的librosa版本是0.6.0              
   

## 2020.3.29

1. 利用Keras训练模型。[训练代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/train.py)
2. 保存模型。[模型下载](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/model.h5)
3. 模型预测。[预测代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/test.py)

## 2020.4.3

1. 分割音频。[核心代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/cutwav.py)
2. 下载Audacity录屏软件，该软件也可以生成指定音频。[下载Audacity](https://www.audacityteam.org/)
3. 将一些音频分割成一两秒，经过模型测试，不满足预期。

### 2020.4.4

1. 分割训练集，初步猜想是因为训练集每段时间太长，将训练集分成2s一段，进行训练，得到的模型不能识别静音文件。
2. 用Audacity生成两个小时的静音文件，分割成2s一段放进训练集的others文件夹，重新训练，模型应用效果有待测试。

