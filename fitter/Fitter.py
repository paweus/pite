import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import scipy

#Klasa Fitter odpowiedzialna za stworzenir dopasowanej funkcji do wygenerowanych danych
class Fitter:
    def __init__(self):
        self.fitted_args = 0
        self.x = []
        self.yn = []
        self.fitted_data = []

    #Funkcja potrzebna do uzycia metody curfe_fit
    #Argumenty: wartosci osi x, amplituda funkcji, czestotliwsc funkcji, przesuniecie fazowe, przesuniecie w osi y
    def func(self,x, amplitude, frequency,offset,move):
        return amplitude*np.sin(frequency*x + offset) + move

    #Funkcja pobierajaca dane i zapisujaca je w obiekcie klasy Fitter
    #Argumenty: wartosci x, wartosci y(zaszumione)
    def getData(self,x,yn):
        self.x = x;
        self.yn = yn;

    #Funkcja generujaca "zgadywane" wartosci argumentow sinusoidy
    #Argumenty: wartosc czestotliwosci (ktora jest iterowana)
    def guess(self,more):
        guess_amplitude = np.std(self.yn)/(2**0.5)
        guess_freq = more
        guess_offset = np.mean(self.yn)
        guess_move = 0
        p0=[guess_amplitude,guess_freq,guess_offset,guess_move]
        return p0

    #Funkcja tworzaca dopasowanie do zestawu danych, z uzyciem zestawu zgadywanych argumentow
    def fit(self,guessData):
        try:
            #Dopasowywanie z uzyciem funkcji curve_fit
            self.fitted_args, pcov = curve_fit(self.func, self.x, self.yn, guessData)
        except:
            print 'Curve_fit Error'
        try:
            self.dataCreator()
        except:
            print 'DataCreator Error'

    #Funkcja tworzaca nowy zestaw danych, dla dopasowanej funkcji
    def dataCreator(self):
        self.fitted_data = self.func(self.x, self.fitted_args[0], self.fitted_args[1],self.fitted_args[2],self.fitted_args[3])

    #Funckja drukujaca dopasowane argumenty funkcji sinus
    def printfitted_args(self):
        return self.fitted_args

    #Funckja zwracajaca dopasowane argumenty funkcji sinus
    def returnfitted_args(self):
        return self.fitted_args

    #Funckja zwracajaca zestaw danych dopasowanej funkcji
    def returnFittedData(self):
        return self.fitted_data
