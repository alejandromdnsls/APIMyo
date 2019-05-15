# coding=utf-8
from dataReader import *
from Sensors import *
from Sample import *

import glob

archivos = glob.glob("Datos/Test/*.xlsx")
samples = list()

for row in archivos:
    sensores = Sensors()
    sample = Sample()
    data = dataReader(row)

    sensores.setClass(row.split('.')[0].split('/')[-1])

    sensores.setVector('emg1', data.read()['emgemg1'])
    sensores.setVector('emg2', data.read()['emgemg2'])
    sensores.setVector('emg3', data.read()['emgemg3'])
    sensores.setVector('emg4', data.read()['emgemg4'])
    sensores.setVector('emg5', data.read()['emgemg5'])
    sensores.setVector('emg6', data.read()['emgemg6'])
    sensores.setVector('emg7', data.read()['emgemg7'])
    sensores.setVector('emg8', data.read()['emgemg8'])
    sensores.setVector('ax', data.read()['accelerometerx'])
    sensores.setVector('ay', data.read()['accelerometery'])
    sensores.setVector('az', data.read()['accelerometerz'])

    print(sensores.getClass())

    sample.standardDeviation(sensores.getEmg())
    sample.segmentation(sensores.getVector('ax'), 'ax')
    sample.segmentation(sensores.getVector('ay'), 'ay')
    sample.segmentation(sensores.getVector('az'), 'az')

    samples.append(sample)

    del sensores
    del sample

print (samples)
