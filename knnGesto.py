# coding=utf-8
from math import sqrt
from operator import itemgetter

class knnGesto:

    def learning(self, samples):
        dbGesto = open('dbGesto.csv','w')
        headers = ['id_gesto', 'name', 'emg1', 'emg2', 'emg3', 'emg4', 'emg5', 'emg6', 'emg7', 'emg8']
        cad = ''
        for head in headers:
            cad = cad + head + ','
        cad = cad[:-1] + '\n'
        dbGesto.write(cad)

        id = 0
        for sample in samples:
            cad = str(id) + ',' + sample.getClass() + ','
            for emg in sample.getStandarDeviation():
                cad = cad + str(emg) + ','
            cad = cad[:-1] + '\n'
            dbGesto.write(cad)

            id = id + 1

        dbGesto.close()

    def recovery(self, sample):
        dbGesto = open('dbGesto.csv','r')
        distances = list()
        for row in dbGesto:
            if row[:-1].split(',')[0] != 'id_gesto':
                aux = row[:-1].split(',')
                distances.append([aux[0], aux[1], self.distance(aux[2:], sample.getStandarDeviation())])
        distances = sorted(distances, key=itemgetter(2))
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
