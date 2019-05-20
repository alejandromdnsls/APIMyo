# coding=utf-8
from math import sqrt
from operator import itemgetter

class knnMove:

    def learning(self, samples):
        dbMove = open('dbMove.csv','w')
        headers = ['id_move', 'name', 'axis', 'seg1', 'seg2', 'seg3', 'seg4', 'seg5', 'seg6', 'seg7', 'seg8', 'seg9', 'seg10', 'seg11', 'seg12', 'seg13', 'seg14', 'seg15', 'seg16', 'seg17', 'seg18', 'seg19', 'seg20', 'seg21', 'seg22', 'seg23', 'seg24', 'seg25', 'seg26', 'seg27', 'seg28', 'seg29', 'seg30', 'seg31', 'seg32']
        cad = ''
        for head in headers:
            cad = cad + head + ','
        cad = cad[:-1] + '\n'
        dbMove.write(cad)

        id = 0
        for sample in samples:
            cad = str(id) + ',' + sample.getClass() + ',X,'
            for seg in sample.getSegmentX():
                cad = cad + str(seg) + ','
            cad = cad[:-1] + '\n'
            dbMove.write(cad)

            cad = str(id) + ',' + sample.getClass() + ',Y,'
            for seg in sample.getSegmentY():
                cad = cad + str(seg) + ','
            cad = cad[:-1] + '\n'
            dbMove.write(cad)

            cad = str(id) + ',' + sample.getClass() + ',Z,'
            for seg in sample.getSegmentZ():
                cad = cad + str(seg) + ','
            cad = cad[:-1] + '\n'
            dbMove.write(cad)
            id = id + 1

        dbMove.close()

    def recovery(self, sample):
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

        return distances[0][0]

    def distance(self, s1, s2):
        result = 0
        for index in range(len(s1)):
            result = result + pow(float(s1[index])-s2[index], 2)
        return sqrt(result)
