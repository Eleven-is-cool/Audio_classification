#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nl8590687
用于测试整个一套语音识别系统的程序
语音模型 + 语言模型
"""
import platform as plat
from SpeechModel251 import ModelSpeech
from LanguageModel2 import ModelLanguage
from keras import backend as K
import sys

if __name__ == '__main__':
	datapath = ''
	modelpath = 'model_speech'

	system_type = plat.system()
	if(system_type == 'Windows'):
		datapath = '.'
		modelpath = modelpath + '\\'
	elif(system_type == 'Linux'):
		datapath = 'dataset'
		modelpath = modelpath + '/'
	else:
		# print('*[Message] Unknown System\n')
		datapath = 'dataset'
		modelpath = modelpath + '/'

	ms = ModelSpeech(datapath)

	ms.LoadModel(modelpath + 'speech_model251_e_0_step_625000.model')

	# r = ms.RecognizeSpeech_FromFile(sys.argv[1])
	r = ms.RecognizeSpeech_FromFile(r"F:\code\Audio_classification\dataBase\UrbanSound8K_byclass\person\A2_4.wav")
	K.clear_session()

	# print('*[提示] 语音识别结果：\n',r)
	ml = ModelLanguage('model_language')
	ml.LoadModel()

	str_pinyin = r
	r = ml.SpeechToText(str_pinyin)
	print(r)














