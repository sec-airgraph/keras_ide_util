# -*- coding: utf-8 -*-
'''
Keras Learning script for Keras-IDE
'''
__author__	= 'Ryuichiro Kodama<kodama@sec.co.jp>'
__version__	= '0.1'
__date__	= '12 Sep 2017'

from logging import getLogger

class DataMaker(object):
	"""
	学習用入力データ作成クラス
	"""
	def __init__(self, logLevel=20):
		"""
		@param logger_ ロガーを外部から指定する場合は設定。指定しなければルートロガーを取得
		"""
		self.logger = getLogger(__name__)
		self.logger.setLevel(logLevel)

	def make_input_data(self):
		"""
		入力データを整形・加工する
		@return 訓練データと検証データの入出力ペア(x_train, y_train), (x_test, y_test)
		"""
		from keras.datasets import mnist
		from keras.utils.np_utils import to_categorical
		self.logger.info("""
			Here
			Here
			Here
			Here
			Here
			Here
			Here
		""")
		###############################################
		# Load data for learning
		# Split the sample data to train data and validation data
		###############################################
		self.logger.info('loading mnist data...')
		(x_train, y_train), (x_test, y_test) = mnist.load_data()
		self.logger.info('mnist data loaded')

		################################################
		# Reshape input data
		################################################
		self.logger.info('reshape data')
		x_train = x_train.reshape(60000, 784)
		x_test = x_test.reshape(10000, 784)
		x_train = x_train.astype('float32')
		x_test = x_test.astype('float32')
		x_train /= 255
		x_test /= 255

		################################################
		# Reshape validation data
		################################################
		num_classes = 10
		y_train = y_train.astype('int32')
		y_test = y_test.astype('int32')
		y_train = to_categorical(y_train, num_classes)
		y_test = to_categorical(y_test, num_classes)

		self.logger.info('all data reshaped')

		return (x_train, y_train), (x_test, y_test)

	def make_test_data(self):
		"""
		検証データを作成する
		@return 訓練データと検証データの入出力ペア x_test, y_test
		"""
		from keras.datasets import mnist
		###############################################
		# Load data for learning
		# Split the sample data to train data and validation data
		###############################################
		self.logger.info('loading mnist data...')
		(x_train, y_train), (x_test, y_test) = mnist.load_data()
		self.logger.info('mnist data loaded')

		################################################
		# Reshape input data
		################################################
		self.logger.info('reshape data')
		x_train = x_train.reshape(60000, 784)
		x_test = x_test.reshape(10000, 784)
		x_train = x_train.astype('float32')
		x_test = x_test.astype('float32')
		x_train /= 255
		x_test /= 255

		################################################
		# Reshape validation data
		################################################
		from keras.utils.np_utils import to_categorical
		num_classes = 10
		y_train = y_train.astype('int32')
		y_test = y_test.astype('int32')
		y_train = to_categorical(y_train, num_classes)
		y_test = to_categorical(y_test, num_classes)

		self.logger.info('all data reshaped')

		return x_test, y_test

	def make_prediction_data(self):
		import os
		import Image
		import numpy
		x_test_list = []
		source_list = []
		for image_file in os.listdir('sample/images'):
			img = Image.open('sample/images/' + image_file).convert('L')
			img.thumbnail((28, 28))
			img = numpy.array(img, dtype=numpy.float32)
			img = 1 - numpy.array(img / 255)
			img = img.reshape(1, 784)
			x_test_list.append(img)
			source_list.append(image_file)
		return x_test_list, source_list
