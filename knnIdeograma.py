# coding=utf-8
from math import sqrt
from operator import itemgetter
from SignMoveConexion import *

class knnIdeograma:

    def learning(self, samples):
        context = signMoveConexion()
        context.insertIdeogram(samples)
        context.closeBD()

    def recovery(self, sample):
        dbIdeogramas = open('dbIdeogramas.csv','r')
        distances = list()

        context = signMoveConexion()
        for row in context.consultaIdeogram():
            distances.append([row[0], row[1], self.distance(row[2:], sample)])

        distances = sorted(distances, key=itemgetter(2))
        return distances[0][1]

    def distance(self, s1, s2):
        result = 0
        for index in range(len(s1)):
            result = result + pow(float(s1[index])-s2[index], 2)
        return sqrt(result)
