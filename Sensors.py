# coding=utf-8

class Sensors:

    def __init__(self):
        self.emg1 = []
        self.emg2 = []
        self.emg3 = []
        self.emg4 = []
        self.emg5 = []
        self.emg6 = []
        self.emg7 = []
        self.emg8 = []
        self.ax = []
        self.az = []
        self.az = []
        self.clase = ''

    def getVector(self, sensor):
        if(sensor == 'emg1'):
            return self.emg1
        elif(sensor == 'emg2'):
            return self.emg2
        elif(sensor == 'emg3'):
            return self.emg3
        elif(sensor == 'emg4'):
            return self.emg4
        elif(sensor == 'emg5'):
            return self.emg5
        elif(sensor == 'emg6'):
            return self.emg6
        elif(sensor == 'emg7'):
            return self.emg7
        elif(sensor == 'emg8'):
            return self.emg8
        elif(sensor == 'ax'):
            return self.ax
        elif(sensor == 'ay'):
            return self.ay
        elif(sensor == 'az'):
            return self.az
        else:
            return None

    def setVector(self, sensor, data):
        if(sensor == 'emg1'):
            self.emg1 = data
        elif(sensor == 'emg2'):
            self.emg2 = data
        elif(sensor == 'emg3'):
            self.emg3 = data
        elif(sensor == 'emg4'):
            self.emg4 = data
        elif(sensor == 'emg5'):
            self.emg5 = data
        elif(sensor == 'emg6'):
            self.emg6 = data
        elif(sensor == 'emg7'):
            self.emg7 = data
        elif(sensor == 'emg8'):
            self.emg8 = data
        elif(sensor == 'ax'):
            self.ax = data
        elif(sensor == 'ay'):
            self.ay = data
        elif(sensor == 'az'):
            self.az = data
        else:
            return None

    def getEmg(self):
        emg = []
        emg.append(self.emg1)
        emg.append(self.emg2)
        emg.append(self.emg3)
        emg.append(self.emg4)
        emg.append(self.emg5)
        emg.append(self.emg6)
        emg.append(self.emg7)
        emg.append(self.emg8)
        
        return emg

    def setClass(self, cad):
        self.clase = cad

    def getClass(self):
        return self.clase


if __name__ == '__main__':
    obj = Sensors()
    obj.setVector('emg1',[1,2,3])
    obj.setVector('emg2',[7,2,3])
    obj.setVector('emg3',[19,0,3])
    obj.setVector('emg4',[61,29,3])
    obj.setVector('emg5',[451,12,53])
    obj.setVector('emg6',[71,922,63])
    obj.setVector('emg7',[91,24,23])
    obj.setVector('emg8',[11,21,13])
    obj.setVector('ax',[3,6,8])
    obj.setVector('ay',[9,5,32])
    obj.setVector('az',[30,12,5])

    print('emg1', obj.getVector('emg1'))
    print('emg2', obj.getVector('emg2'))
    print('emg3', obj.getVector('emg3'))
    print('emg4', obj.getVector('emg4'))
    print('emg5', obj.getVector('emg5'))
    print('emg6', obj.getVector('emg6'))
    print('emg7', obj.getVector('emg7'))
    print('emg8', obj.getVector('emg8'))
    print('ax', obj.getVector('ax'))
    print('ay', obj.getVector('ay'))
    print('az', obj.getVector('az'))

    obj.setClass('Hola')
    print(obj.getClass())
