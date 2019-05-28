# coding=utf-8
from math import sqrt
from operator import itemgetter
from SignMoveConexion import *

class knnMove:

    def learning(self, samples):
        context = signMoveConexion()
        context.insertMove(samples)
        context.closeBD()

    def recovery(self, sample):
        distances = list()
        context = signMoveConexion()
        for row in context.consultaMove():
            if row[2] == 'x':
                distances.append([row[0], row[1], self.distance(row[3:], sample.getSegmentX())])
            elif row[2] == 'Y':
                distances.append([row[0], row[1], self.distance(row[3:], sample.getSegmentY())])
            elif row[2] == 'Z':
                distances.append([row[0], row[1], self.distance(row[3:], sample.getSegmentZ())])

        out = dict()
        for distance in distances:
            if distance[1] in out:
                out[distance[1]][2] = out[distance[1]][2] + distance[2]
            else:
                out[distance[1]] = [distance[0], distance[1], distance[2]]

        distances = list()
        for key in out:
            distances.append(out[key])
        distances = sorted(distances, key=itemgetter(2))

        context.closeBD()

        return distances[0][0]

    def recClass(self,sample):
        dbMove = open('dbMove.csv','r')
        distances = list()
        for row in dbMove:
            if row[:-1].split(',')[0] != 'id_move':
                aux = row[:-1].split(',')
                if aux[2] == 'X':
                    distances.append([aux[0], aux[1], self.distance(aux[3:], sample.getSegmentX())])
                elif aux[2] == 'Y':
                    distances.append([aux[0], aux[1], self.distance(aux[3:], sample.getSegmentY())])
                elif aux[2] == 'Z':
                    distances.append([aux[0], aux[1], self.distance(aux[3:], sample.getSegmentZ())])
        out = dict()
        for distance in distances:
            if distance[1] in out:
                out[distance[1]][2] = out[distance[1]][2] + distance[2]
            else:
                out[distance[1]] = [distance[0], distance[1], distance[2]]

        distances = list()
        for key in out:
            distances.append(out[key])
        distances = sorted(distances, key=itemgetter(2))

        return distances[0][1]

    def distance(self, s1, s2):
        result = 0
        for index in range(len(s1)):
            result = result + pow(float(s1[index])-s2[index], 2)
        return sqrt(result)
