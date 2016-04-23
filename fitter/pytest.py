import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
from scipy import stats
import scipy

class Generator:
    def __init__(self):
        self.amplitude = 1
        self.frequency = 2
        self.offset = 1
        self.noise_offset = 0.5
        self.noise_level = 1000
        self.x = []
        self.y = []
        self.yn = []
        self.move = 30

    def creator(self):
        # Generating clean data
        self.x = np.linspace(0, 10, self.noise_level)
        self.y = self.amplitude*np.sin(self.frequency*self.x + self.offset) + self.move

        # Adding noise to the data
        self.yn = self.y + self.noise_offset * np.random.normal(size=len(self.x))

    def returnX(self):
        return self.x
    def returnYn(self):
        return self.yn
    def returnY(self):
        return self.y

class Fitter:
    def __init__(self):
        self.popt = 0
        self.x = []
        self.yn = []
        self.fitted_data = []

    @staticmethod
    def func(x, amplitude, frequency,offset,move):
        return amplitude*np.sin(frequency*x + offset) + move

    def setData(self,x,yn):
        self.x = x;
        self.yn = yn;

    def fit(self):
        self.popt, pcov = curve_fit(Fitter.func, self.x, self.yn)
        self.dataCreator()


    def dataCreator(self):
        self.fitted_data = Fitter.func(self.x, self.popt[0], self.popt[1],self.popt[2],self.popt[3])

    def printPopt(self):
        print self.popt

    def returnPopt(self):
        return self.popt

    def returnFittedData(self):
        return self.fitted_data


class Plotter:
    def plot(self,x,y,yn,fitted_data):
        fig = mpl.figure()
        ax = fig.add_subplot(111)
        ax.scatter(x, yn,c='g',s=10,edgecolor='green',label='Data')
        ax.plot(x, fitted_data, c='r',linewidth=4.0, label='Best fit')
        ax.plot(x, y, c='b',linewidth=1.0, label='Function')
        ax.legend()
        mpl.xlim((0,10))
        mpl.show()

class Main:
    gen = Generator()
    gen.creator()
    fit = Fitter()
    fit.setData(gen.returnX(),gen.returnYn())
    fit.fit()
    fit.printPopt()
    plot = Plotter()
    plot.plot(gen.returnX(),gen.returnY(),gen.returnYn(),fit.returnFittedData())
