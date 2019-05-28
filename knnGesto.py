# coding=utf-8
from math import sqrt
from operator import itemgetter
from SignMoveConexion import *

class knnGesto:

    def learning(self, samples):
        context = signMoveConexion()
        context.insertSign(samples)
        #context.closeBD()

    def recovery(self, sample):
        distances = list()
        context = signMoveConexion()
        for registro in context.consultaSign():
            distances.append([registro[0], registro[1], self.distance(registro[2:], sample.getStandarDeviation())])
        distances = sorted(distances, key = itemgetter(2))
        #context.closeBD()
        return distances[0][0]

    def recClass(self,sample):
        dbGesto = open('dbGesto.csv','r')
        distances = list()
        for row in dbGesto:
            if row[:-1].split(',')[0] != 'id_gesto':
                aux = row[:-1].split(',')
                distances.append([aux[0], aux[1], self.distance(aux[2:], sample.getStandarDeviation())])
        distances = sorted(distances, key=itemgetter(2))
        return distances[0][1]

    def distance(self, s1, s2):
        result = 0
        for index in range(len(s1)):
            result = result + pow(float(s1[index])-s2[index], 2)
        return sqrt(result)
