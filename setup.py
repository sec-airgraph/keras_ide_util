# -*- coding: utf-8 -*-
'''
setup for Keras Learning script for Keras-IDE
'''
from setuptools import setup, find_packages

setup(
	name='keras_ide_util',
	version='0.1',
	description='Keras Execution Package for Keras-IDE',
	long_description=open('README.md').read(),
	author='Ryuichiro Kodama',
	author_email='kodama@sec.co.jp',
	packages=find_packages(exclude=['sample']),
	entry_points={
		"console_scripts":[
			"keras-ide-util=keras_ide_util.__main__:main"
		]
	},
	zip_safe = False
)
