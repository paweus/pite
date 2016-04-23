import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
from scipy import stats
import scipy

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


    def getData(self,amp,frequency,noise_points,noise_rozrzut,offset,od,do):
        self.od = od
        self.do = do
        self.amplitude = amp
        self.frequency = frequency
        self.noise_points = noise_points
        self.noise_rozrzut = noise_rozrzut
        self.offset = offset

    def guess(self,more):
        guess_amplitude = np.std(self.yn)/(2**0.5)
        guess_freq = more
        guess_offset = np.mean(self.yn)
        guess_move = 0
        p0=[guess_amplitude,guess_freq,guess_offset,guess_move]
        return p0

    def creator(self):
        # Generating clean data
        self.x = np.linspace(self.od, self.do, self.noise_points)
        self.y = self.amplitude*np.sin(self.frequency*self.x + self.offset) + self.move

        # Adding noise to the data
        self.yn = self.y + self.noise_rozrzut * np.random.normal(size=len(self.x))

    def returnX(self):
        return self.x
    def returnYn(self):
        return self.yn
    def returnY(self):
        return self.y
