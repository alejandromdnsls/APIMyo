# coding=utf-8
import math
from SignMoveConexion import *

class Sample:

    def __init__(self):
        self.standardDev = list()
        self.segmentX = list()
        self.segmentY = list()
        self.segmentZ = list()
        self.clase = ''

    def arithmeticMean(self, vals):
        val = 0
        for value in vals:
            val = val + value
        return val / len(vals)

    def standardDeviation(self, vals):
        #print(vals)
        for sensor in vals:
            val = 0
            #print(sensor)
            mean = self.arithmeticMean(sensor)
            for value in sensor:
                val = val + pow(abs(value - mean), 2)
            val = math.sqrt(val / len(sensor))
            self.standardDev.append(val)
        #print(self.standardDev)

    def getStandarDeviation(self):
        return self.standardDev

    def getSegmentX(self):
        return self.segmentX

    def getSegmentY(self):
        return self.segmentY

    def getSegmentZ(self):
        return self.segmentZ


    def segmentation(self, vals, axis):
        aux = list()
        for index in range(10,len(vals)+1):
            suma = 0
            for num in range(index-10, index):
                suma = suma + vals[num]
            aux.append(suma/10)
        #print (aux)
        aux1 = list()
        for rango in range(0, len(aux), 10):
            m = 0
            try:
                for ran in range(rango, rango + 10):
                    m = m + aux[ran]
            except IndexError:
                m = 0
                for ran in range(rango, len(aux)):
                    m = m + aux[ran]
            m = m / 10
            aux1.append(m)
        if axis == 'ax':
            self.segmentX = aux1
        elif axis == 'ay':
            self.segmentY = aux1
        elif axis == 'az':
            self.segmentZ = aux1
        del aux
        del aux1
        #print(aux1)

    def setClass(self, clase):
        self.clase = clase

    def getClass(self):
        return self.clase
