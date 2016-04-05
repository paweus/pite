import numpy as np
import csv

#Prosta klasa czytajaca dane z pliku do wizualizacji
class Reader:
    def __init__(self):
        load = 0
        load2 = 0

    #Funkcja czytajaca dane
    @staticmethod
    def read(path):
        Reader.load = np.genfromtxt(str(path), delimiter=',')
        Reader.load2 = np.genfromtxt(str(path), delimiter=',',dtype=str)
        print 'Data reading complete'
