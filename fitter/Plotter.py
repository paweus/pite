import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl

#Klasa odpowiedzialna za rysowanie wykresu funkcji
class Plotter:
    poczatkowa = True
    dopasowana = True
    dane = True
    xlim_min = 0
    xlim_max = 10
    def __init__(self):
        self.fig = mpl.figure()

    #Funkcja rysujaca wykres
    #Argumenty: wartosci x, wartosci y(funkcji poczatkowej), wartosci yn(wartosci zaszumione), wartosci dopasowanej funkcji
    def plot(self,x,y,yn,fitted_data):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        #Rysuje na wykresie zaszumione dane, jesli opcja jest zaznaczona
        if(Plotter.dane):
            ax.scatter(x, yn,c='g',s=10,edgecolor='green',label='Data')
        #Rysuje na wykresie funkcje dopasowana, jesli opcja jest zaznaczona
        if(Plotter.dopasowana):
            ax.plot(x, fitted_data, c='r',linewidth=4.0, label='Dopasowanie')
        #Rysuje na wykresie funkcje poczatkowa, jesli opcja jest zaznaczona
        if(Plotter.poczatkowa):
            ax.plot(x, y, c='b',linewidth=1.0, label='Funkcja')
        ax.legend(prop={'size':10})
        mpl.xlim((Plotter.xlim_min,Plotter.xlim_max))
        return self.fig
