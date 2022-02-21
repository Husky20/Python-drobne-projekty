import time
import datetime
import threading, queue

SizePlane = 3


def log(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print("%s %s" % (now, message))

def oblicz(x):
    time.sleep(x)
    return x * x

print("Hello world")
#TODO: zacznij nalizę mojego repo i napisz funkcję stan
class Stan:
    '''
    Klasa przechowująca stany
    '''
    def __init__(self, previewStan = None):
        if previewStan:
            self.Plane = previewStan.GetPlane()
        else:
            self.Plane = [[0] * SizePlane for i in range(SizePlane)]

def Szukaj():
    '''
    Główna funkcja programu
    :return:
    '''
    pass