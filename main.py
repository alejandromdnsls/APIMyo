# coding=utf-8
from dataReader import *
from Sensors import *
from Sample import *
from LearningSet import *
import glob

archivos = glob.glob("Datos/Test/*.xlsx")
samples = list()

aux = Sensors()

for row in archivos:
    sensores = Sensors()
    sample = Sample()
    data = dataReader(row)

    sensores.setClass(row.split('.')[0].split('/')[-1].split('_')[0])


    sensores.setVector('ax', data.read()[0])
    sensores.setVector('ay', data.read()[1])
    sensores.setVector('az', data.read()[2])
    sensores.setVector('emg1', data.read()[3])
    sensores.setVector('emg2', data.read()[4])
    sensores.setVector('emg3', data.read()[5])
    sensores.setVector('emg4', data.read()[6])
    sensores.setVector('emg5', data.read()[7])
    sensores.setVector('emg6', data.read()[8])
    sensores.setVector('emg7', data.read()[9])
    sensores.setVector('emg8', data.read()[10])

    #print(sensores.getClass())

    sample.setClass(sensores.getClass())
    sample.standardDeviation(sensores.getEmg())
    sample.segmentation(sensores.getVector('ax'), 'ax')
    sample.segmentation(sensores.getVector('ay'), 'ay')
    sample.segmentation(sensores.getVector('az'), 'az')

    samples.append(sample)

    aux = sensores

    del sensores
    del sample


i = len(samples)/100
ls = LearningSet()

ls.setValues(samples[:int(i*70)])
print(len(ls.getValues()))
"""for num in range(int(i*70),len(samples)):
    print (num)
"""
