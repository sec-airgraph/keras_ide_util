# -*- coding: utf-8 -*-
'''
Keras Learning script for Keras-IDE
'''
__author__	= 'Ryuichiro Kodama<kodama@sec.co.jp>'
__version__	= '0.1'
__date__	= '12 Sep 2017'

def parser(logger):
	"""
	コマンドライン引数処理
	@return command, args 実行コマンドとコマンドに対するオプション引数
	"""
	from argparse import ArgumentParser
	# トップレベルコマンド
	argparser = ArgumentParser()
	subparsers = argparser.add_subparsers(help='command help')
	# サブコマンド：learn
	learn_parser = subparsers.add_parser('learn', help='execute learning')
	learn_parser.add_argument('FILE', help='json file path of the model for learning')
	learn_parser.add_argument('-m', '--maker', type=str, dest='data_maker', default=None, help='data_maker module file including DataMaker class')
	learn_parser.add_argument('-o', '--out', type=str, dest='result_path', default='./result.hdf5', help='path to save .hdf5')
	learn_parser.add_argument('-l', '--log', type=str, dest='log_dir_path', default='/data/tensorflow_log/', help='log dir for tensorboard')
	learn_parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose message')
	learn_parser.set_defaults(command='learn')
	# サブコマンド：evaluate
	evaluate_parser = subparsers.add_parser('evaluate', help='execute evaluation')
	evaluate_parser.add_argument('FILE', help='hdf5 file path of the model for evaluation')
	evaluate_parser.add_argument('-m', '--maker', type=str, dest='data_maker', default=None, help='data_maker module file including DataMaker class')
	evaluate_parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose message')
	evaluate_parser.set_defaults(command='evaluate')
	# サブコマンド：predict
	predict_parser = subparsers.add_parser('predict', help='execute prediction')
	predict_parser.add_argument('FILE', help='hdf5 file path of the model for prediction')
	predict_parser.add_argument('-m', '--maker', type=str, dest='data_maker', default=None, help='data_maker module file including DataMaker class')
	predict_parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose message')
	predict_parser.set_defaults(command='predict')

	args = argparser.parse_args()
	# --verboseのときはDEBUG以上を見せる
	if args.verbose:
		logger.setLevel(10)
	else:
		logger.setLevel(20)

	return args

def main():
	"""
	コマンドラインから呼び出すためのメソッド
	"""
	import logging
	import os
	logging.basicConfig()
	logger = logging.getLogger(__name__)
	args = parser(logger)
	logger.debug(os.getcwd())
	from keras_ide_util.keras_ide_utils import KerasIdeUtils
	utils = KerasIdeUtils(logger.getEffectiveLevel(), args.data_maker)
	if args != None:
		if args.command == 'learn':
			utils.learn(args.FILE, args.log_dir_path, args.result_path)
		elif args.command == 'evaluate':
			utils.evaluate(args.FILE)
		elif args.command == 'predict':
			utils.predict(args.FILE)

if __name__ == '__main__':
	main()
