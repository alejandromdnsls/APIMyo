# coding=utf-8
from Sample import *


class LearningSet:

    def __init__ (self):
        self.samples = dict()

    def setValues(self, samples):
        for sample in samples:
            if sample.getClass() in self.samples:
                self.samples[sample.getClass()].append(sample)
            else:
                self.samples[sample.getClass()] = [sample]
        self.samples = self.doAvg()

    def doAvg(self):
        out = dict()
        for key in self.samples:
            for sample in self.samples[key]:
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
                out[key][val] = out[key][val] / len(self.samples[key])
        return out

    def getValues(self):
        return self.samples
