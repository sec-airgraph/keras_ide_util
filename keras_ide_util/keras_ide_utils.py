# -*- coding: utf-8 -*-
'''
Keras Learning script for Keras-IDE
'''
__author__	= 'Ryuichiro Kodama<kodama@sec.co.jp>'
__version__	= '0.1'
__date__	= '12 Sep 2017'

import keras
from logging import getLogger

class KerasIdeUtils(object):
	"""
	Keras-IDEで作成したモデルから各種Kerasの処理を実行する
	"""
	def __init__(self, logLevel=20, original_data_maker=None):
		"""
		@param logger_ ロガーを外部から指定する場合は設定。指定しなければルートロガーを取得
		"""
		self.logger = getLogger(__name__)
		self.logger.setLevel(logLevel)
		if (original_data_maker is None):
			self.logger.debug('original data maker is "None"')
			from keras_ide_util.data_maker import DataMaker
			self.data_maker = DataMaker()
		else:
			self.logger.debug('original data maker is "{}"'.format(original_data_maker))
			import imp
			self.data_maker = imp.load_source('data_maker', original_data_maker).DataMaker()

	def load_model_from_ide(self, json_file_path):
		"""
		Keras-IDEで作成したモデルの読み込み
		"""
		################################################
		# Load model
		################################################
		self.logger.info('load model from json file')
		self.logger.debug('json file:' + json_file_path)
		import json

		# 学習プロパティ類取得のため生JSONも取得
		json_file = open(json_file_path)
		model_json = json_file.read()
		model_json_object = json.loads(model_json)
		json_file.close()
		# モデル読み込み
		keras_model = keras.models.model_from_json(model_json)
		self.logger.info('model loaded')
		keras_model.summary()
		return keras_model, model_json_object

	def evaluate(self, model_file_path):
		"""
		学習結果の評価
		@param model_file_path 重み付きモデルファイル（.hdf5）へのパス
		@param x_test テストデータ(入力)
		@param y_test テストデータ（出力）
		"""
		from keras.models import load_model
		# IDEで作成したモデルのJSON読み込み
		keras_model = load_model(model_file_path)
		# テストデータの読み込み
		x_test, y_test = self.data_maker.make_test_data()
		################################################
		# Evaluate leaning result
		################################################
		score = keras_model.evaluate(x_test, y_test, verbose=1)
		self.logger.info('Test loss:{}'.format(score[0]))
		self.logger.info('Test accuracy:{}'.format(score[1]))


	def learn(self, model_json_file_path, log_dir_path, result_path):
		"""
		学習実行
		@model_json_file_path	Keras-IDEで作成したモデルのJSONファイルへのパス
		@log_dir_path			TensorBoard用のログ吐き出し先のディレクトリパス
		@result_path			学習結果のhdf5ファイル保存先ファイルパス
		"""
		(x_train, y_train), (x_test, y_test) = self.data_maker.make_input_data()
		# IDEで作成したモデルのJSON読み込み
		keras_model, model_json_object = self.load_model_from_ide(model_json_file_path)
		################################################
		# Set callbacks for TensorBoard
		################################################
		callbacks = []
		# for callback in model_json_object['fit.callback']:
		# 	callbacks.append(keras.callbacks[callback])
		callbacks.append(keras.callbacks.EarlyStopping(monitor='val_loss', patience=0, verbose=0, mode='auto'))
		callbacks.append(keras.callbacks.TensorBoard(log_dir=log_dir_path, histogram_freq=1))

		################################################
		# Set learning properties
		################################################
		optimizer = model_json_object['optimizer']
		loss = model_json_object['loss']
		metrics = model_json_object['metrics']

		keras_model.compile(loss=loss, optimizer=optimizer, metrics=metrics)

		################################################
		# Execute leaning
		################################################
		# バッチサイズ、エポック数
		batch_size = model_json_object['fit.batch_size']
		epochs = model_json_object['fit.epochs']

		history = keras_model.fit(x_train, y_train,
							batch_size=batch_size,
							epochs=epochs,
							verbose=1,
							validation_data=(x_test, y_test),
							callbacks=callbacks)

		# 学習結果をsdf5に保存
		keras_model.save(result_path)

		################################################
		# Evaluate leaning result
		################################################
		score = keras_model.evaluate(x_test, y_test, verbose=1)
		self.logger.info('Test loss:{}'.format(score[0]))
		self.logger.info('Test accuracy:{}'.format(score[1]))

	def predict(self, model_file_path):
		"""
		予測実行
		@model_json_file_path	Keras-IDEで作成したモデルのJSONファイルへのパス
		@log_dir_path			TensorBoard用のログ吐き出し先のディレクトリパス
		@result_path			学習結果のhdf5ファイル保存先ファイルパス
		"""
		from keras.models import load_model
		# IDEで作成したモデルのJSON読み込み
		keras_model = load_model(model_file_path)
		# テストデータの読み込み
		x_test_list, source_list = self.data_maker.make_prediction_data()
		################################################
		# Predict
		################################################
		import numpy
		for i in range(len(x_test_list)):
			score = keras_model.predict(x_test_list[i], verbose=0)
			self.logger.debug('data:{}'.format(x_test_list[i]))
			self.logger.debug('score : {}'.format(score))
			self.logger.info('prediction : {} ({})'.format(numpy.argmax(score), source_list[i]))
