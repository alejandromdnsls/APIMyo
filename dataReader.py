# coding=utf-8
from openpyxl import load_workbook

class dataReader:

    def __init__(self,route):
        self.wb = load_workbook(route)
        self.ws = self.wb.active

    def read(self):
        indCol = 0
        out = dict()
        words = ['accelerometerx', 'accelerometery', 'accelerometerz', 'emgemg1', 'emgemg2', 'emgemg3', 'emgemg4', 'emgemg5', 'emgemg6', 'emgemg7', 'emgemg8']
        for col in self.ws.iter_cols(min_row=2):
            for cell in col:
                key = self.ws[1][indCol].value
                if key in words:
                    if cell.value == None:
                        break
                    if key in out:
                        out[key].append(cell.value)
                    else:
                        out[key] = [cell.value]
            indCol = indCol + 1
        return out

if __name__ == '__main__':
    datos = dataReader('Datos/Muestra/a10.xlsx')
    print(datos.read())
