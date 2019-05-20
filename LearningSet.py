# coding=utf-8
from Sample import *

class LearningSet:

    def __init__ (self):
        self.samples = list()

    def setValues(self, samples):
        out = dict()
        for sample in samples:
            if sample.getClass() in out:
                out[sample.getClass()].append(sample)
            else:
                out[sample.getClass()] = [sample]
        out = self.doAvg(out)
        for key in out:
            aux = Sample()
            aux.setClass(key)
            aux.setStandarDeviation(out[key][:8])
            aux.setSegment(out[key][8:40],'X')
            aux.setSegment(out[key][40:72],'Y')
            aux.setSegment(out[key][72:],'Z')
            self.samples.append(aux)
            del aux
        #self.store()

    def doAvg(self, data):
        out = dict()
        for key in data:
            for sample in data[key]:
                if key in out:
                    for emg in range(len(sample.getStandarDeviation())):
                        out[key][emg] = out[key][emg] + sample.getStandarDeviation()[emg]
                    for segment in range(len(sample.getSegmentX())):
                        out[key][8+segment] = out[key][8+segment] + sample.getSegmentX()[segment]
                    for segment in range(len(sample.getSegmentY())):
                        out[key][40+segment] = out[key][40+segment] + sample.getSegmentY()[segment]
                    for segment in range(len(sample.getSegmentZ())):
                        out[key][72+segment] = out[key][72+segment] + sample.getSegmentZ()[segment]
                else:
                    out[key] = sample.getStandarDeviation() + sample.getSegmentX() + sample.getSegmentY() + sample.getSegmentZ()

            for val in range(len(out[key])):
                out[key][val] = out[key][val] / len(data[key])
        return out

    def getValues(self):
        return self.samples

    def store(self):
        for key in self.samples:
            print (key)
        """context = signMoveConexion()
        context.insert(self.samples)
        context.closeBD()"""
