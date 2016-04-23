import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
from scipy import stats
import scipy

#Klasa odpowiedzialna za generowanie zaszumionych danych
class Generator:
    def __init__(self):
        self.amplitude = 0
        self.frequency = 0
        self.noise_points = 0
        self.noise_rozrzut = 0
        self.offset = 0
        self.x = []
        self.y = []
        self.yn = []
        self.move = 30
        self.od = 0
        self.do = 0
        self.guessData =[]

    #Funkcja pobierajaca dane do generatora
    #Argumenty: amplituda, czestotliwosc, ilosc punktow w zaszumionych danych, rozrzut zaszumionych danych, przesuniecie, zakresy rysowania na wykresie
    def getData(self,amp,frequency,noise_points,noise_rozrzut,offset,od,do):
        self.od = od
        self.do = do
        self.amplitude = amp
        self.frequency = frequency
        self.noise_points = noise_points
        self.noise_rozrzut = noise_rozrzut
        self.offset = offset

    #Funkcja generujaca zaszumione dane
    def creator(self):
        #Generowanie zakresu danych osi x
        self.x = np.linspace(self.od, self.do, self.noise_points)

        #Generowaie danych funkcji sinus
        self.y = self.amplitude*np.sin(self.frequency*self.x + self.offset) + self.move

        #dodawanie szumu do danych funkcji sinus
        self.yn = self.y + self.noise_rozrzut * np.random.normal(size=len(self.x))

    #Gettery
    def returnX(self):
        return self.x
    def returnYn(self):
        return self.yn
    def returnY(self):
        return self.y
