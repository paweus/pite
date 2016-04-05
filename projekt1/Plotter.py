import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
import os

#Klasa, ktora zawiera funkcje rysujaca wykresy
class Plotter:

    checkbox_min = 0
    checkbox_max = 0
    counter = 0
    def __init__(self):
        self.data = 0


    #Inicjalizacja danych
    def addData(self,data):
        self.data = data

    #Funkcja rysujaca wykresy
    #argumenty: tytyl wykresu, tytul osi x, tylul osi y, wartosci odpowiadajaca indeksowi w tablicy data dla osi x y
    #Jedna funkcja aby rzadzic wszystkimi wykresami
    def PlotCreator(self,title,title_x,title_y,valuex,valuey):
        self.value_x = []
        self.value_y = []
        self.dev = Plotter.checkbox_max - Plotter.checkbox_min

        for x,y in zip(self.data[:,valuex],self.data[:,valuey]):
            #Okrawanie danych w granicach spinboxow
            if x > Plotter.checkbox_min and x < Plotter.checkbox_max:
                self.value_x.append(x)
                self.value_y.append(y)
        fig = plt.figure()
        plt.plot(self.value_x, self.value_y)
        plt.title(title)
        plt.xlabel(title_x)
        plt.ylabel(title_y)

        plt.xlim((Plotter.checkbox_min,Plotter.checkbox_max))
        plt.xticks((Plotter.checkbox_min,Plotter.checkbox_min + self.dev*0.2,Plotter.checkbox_min + self.dev*0.4,Plotter.checkbox_min + self.dev*0.6,Plotter.checkbox_min + self.dev*0.8,Plotter.checkbox_max))
        plt.grid(True)
        self.CheckDirectory()
        plt.savefig("images/image_"+str(Plotter.counter)+".png")
        Plotter.counter +=1
        return fig

    #Funkcja tworzy folder images, jesli go nie ma
    def CheckDirectory(self):
        if not os.path.exists("images"):
            os.makedirs("images")
