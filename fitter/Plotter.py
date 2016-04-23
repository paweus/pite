import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
import os
import datetime

#Klasa odpowiedzialna za rysowanie wykresu funkcji oraz zapisywanie wykresow do pliku
class Plotter:
    counter = 0
    poczatkowa = True
    dopasowana = True
    dane = True
    xlim_min = 0
    xlim_max = 10
    def __init__(self):
        self.fig = mpl.figure(facecolor="white",figsize=(10, 6))
        self.i = datetime.datetime.now()

    #Funkcja rysujaca wykres
    #Argumenty: wartosci x, wartosci y(funkcji poczatkowej), wartosci yn(wartosci zaszumione), wartosci dopasowanej funkcji
    def plot(self,x,y,yn,fitted_data):
        mpl.clf()
        mpl.close()
        self.fig = mpl.figure(facecolor="white",figsize=(10, 6))
        ax = self.fig.add_subplot(111)
        #Rysuje na wykresie zaszumione dane, jesli opcja jest zaznaczona
        if(Plotter.dane):
            ax.scatter(x, yn,c='g',s=10,edgecolor='green',label='Dane')
        #Rysuje na wykresie funkcje dopasowana, jesli opcja jest zaznaczona
        if(Plotter.dopasowana):
            ax.plot(x, fitted_data, c='r',linewidth=4.0, label='Dopasowanie')
        #Rysuje na wykresie funkcje poczatkowa, jesli opcja jest zaznaczona
        if(Plotter.poczatkowa):
            ax.plot(x, y, c='b',linewidth=1.0, label='Funkcja podst.')
        ax.legend(prop={'size':10})
        mpl.xlim((Plotter.xlim_min,Plotter.xlim_max))

        self.timePlot = str(self.i.strftime('%Y-%m-%d_%H_%M_%S'))
        self.CheckDirectory()
        mpl.savefig("images/" + self.timePlot + "/plot_"+str(Plotter.counter)+".png")
        Plotter.counter += 1
        return self.fig

    #Funckja tworzaca foldery images(jesli nie ma) oraz foldery z aktualna data (tworzona przy uruchomieniu programu)
    #do ktorego zapisuje wykresy.
    #Przy kazdym uruchomieniu programu tworzy nowy folder
    def CheckDirectory(self):
        if not os.path.exists("images"):
            os.makedirs("images")
        if not os.path.exists("images/"+self.timePlot):
            os.makedirs("images/"+self.timePlot)
