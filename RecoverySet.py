# coding=utf-8
from Sample import *

class RecoverySet:

    def __init__ (self):
        self.samples = list()

    def setValues(self, samples):
        for sample in samples:
            self.samples.append(sample)

    def getValues(self):
        return self.samples
