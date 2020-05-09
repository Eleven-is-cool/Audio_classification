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

## 2020.4.4

1. 分割训练集，初步猜想是因为训练集每段时间太长，将训练集分成2s一段，进行训练，得到的模型不能识别静音文件。
2. 用Audacity生成两个小时的静音文件，分割成2s一段放进训练集的others文件夹，重新训练，模型应用效果有待测试。

## 2020.4.8

1. 音频降噪。  [代码](https://github.com/Eleven-is-cool/Audio_classification/tree/master/Enhance_speach)
2. 导入音频显示波形图。[代码](https://github.com/Eleven-is-cool/Audio_classification/blob/master/Data/Merge.py)

## 2020.4.9

1. 合并音频。

## 2020.4.11

1. ~~初次将降噪，切割，识别结合在一起。[Package文件夹](https://github.com/Eleven-is-cool/Audio_classification/tree/master/Package)~~

## 2020.4.16

1. 改写合并音频代码，使其可以根据返回的列表合并音频
2. 编写导入导出音频的格式转换，暂时支持MP3、ogg、wav格式
3. 增加麦克风录入功能，用户可直接录入音频

## 2020.4.17

1. 将目前实现的模块打包。 [Package文件夹](https://github.com/Eleven-is-cool/Audio_classification/tree/master/Package) 
2. 实现web api，可以部署到服务器，但是识别前得先要把 [文件上传](https://github.com/Eleven-is-cool/Audio_classification/blob/master/API/uploadFile.py) 到服务器，这也就导致了只能应用于识别短时音频。[API](https://github.com/Eleven-is-cool/Audio_classification/tree/master/API)

## 2020.4.28

1. 修改训练集：在others中加入大自然相关音频的数据集进行训练，得到model0428.h5

##  2020.5.1

1. 音频分类加载模型更改为REST API的形式，后面识别通过get请求访问本机的API来获取识别结果。
2. 修改多音频文件识别出错的问题。
3. 修改训练集，将others中的无声音频改为1s。
4. 将语音识别更改为REST API的形式打包，后面识别通过get请求访问本机的API来获取识别结果。

## 2020.5.4

1. 清洗数据集，将数据集采样率全部改成22050HZ
2. 重新训练模型，之前模型并不能用于实际应用中。