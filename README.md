# Keras Executor for Keras-IDE

Keras Execution Package for Keras-IDE.

## Installing
```
sudo python setup.py install
```
To check the installation, you just type in the command-line,
```
keras-ide-util --help
```
and you can see the message below.
```
usage: keras-ide-util [-h] {learn,evaluate,predict} ...

positional arguments:
  {learn,evaluate,predict}
                        command help
    learn               execute learning
    evaluate            execute evaluation
    predict             execute prediction

optional arguments:
  -h, --help            show this help message and exit
```

## Sample
You can run a sample with [the scripts](sample).

1. keras-ide-util learn
    * command
        ```
        $ keras-ide-util learn sample/jsonsample.json -m sample/data_maker_sample.py -o sample/result.hdf5
        ```
2. keras-ide-util evaluate
    * command
        ```
        $ keras-ide-util evaluate sample/result.hdf5 -m sample/data_maker_sample.py
        ```
    * result
        ```
        INFO:data_maker:loading mnist data...
        INFO:data_maker:mnist data loaded
        INFO:data_maker:reshape data
        INFO:data_maker:all data reshaped
        9696/10000 [============================>.] - ETA: 0sINFO:keras_ide_util.keras_ide_utils:Test loss:0.0801930498659
        INFO:keras_ide_util.keras_ide_utils:Test accuracy:0.975
        ```
3. keras-ide-util predict
    * command
        ```
        $ keras-ide-util predict sample/result.hdf5 -m sample/data_maker_sample.py
        ```
    * result
        ```
        INFO:keras_ide_util.keras_ide_utils:prediction : 3 (3.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 2 (4.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 2 (2.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 7 (1.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 5 (5.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 6 (6.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 0 (0.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 8 (8.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 2 (7.jpg)
        INFO:keras_ide_util.keras_ide_utils:prediction : 8 (9.jpg)
        ```

## Author
- Ryuichiro Kodama - System Engineering Consultants Co., LTD. -
	[mail](kodama@sec.co.jp)