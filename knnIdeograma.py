# coding=utf-8
from math import sqrt
from operator import itemgetter

class knnIdeograma:

    def learning(self, samples):
        out = dict()
        dbIdeogramas = open('dbIdeogramas.csv','w')
        headers = ['id_ideograma', 'name', 'id_gesto', 'id_move']
        cad = ''
        for head in headers:
            cad = cad + head + ','
        cad = cad[:-1] + '\n'
        dbIdeogramas.write(cad)

        id = 0
        for sample in samples:
            cad = str(id) + ',' + sample[0] + ',' + str(sample[1]) + ',' + str(sample[2]) +'\n'
            dbIdeogramas.write(cad)
            id = id + 1

        """for sample in samples:
            if sample[0] in out:
                out[sample[0]].append([sample[1], sample[2]])
            else:
                out[sample[0]] = [[sample[1], sample[2]]]
        for key in out:
            aux = [0,0]
            for coord in out[key]:
                aux[0] = aux[0] + coord[0]
                aux[1] = aux[1] + coord[1]
            out[key] = [aux[0]/len(out[key]), aux[1]/len(out[key])]

        id = 0
        for key in out:
            cad = str(id) + ',' + key + ',' + str(out[key][0]) + ',' + str(out[key][1]) +'\n'
            dbIdeogramas.write(cad)
            id = id + 1
        """
        dbIdeogramas.close()

    def recovery(self, sample):
        dbIdeogramas = open('dbIdeogramas.csv','r')
        distances = list()
        for row in dbIdeogramas:
            if row[:-1].split(',')[0] != 'id_ideograma':
                aux = row[:-1].split(',')
                distances.append([aux[0], aux[1], self.distance(aux[2:], sample)])
        distances = sorted(distances, key=itemgetter(2))
        return distances[0][1]

    def distance(self, s1, s2):
        result = 0
        for index in range(len(s1)):
            result = result + pow(float(s1[index])-s2[index], 2)
        return sqrt(result)
