import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import scipy
class Fitter:
    def __init__(self):
        self.popt = 0
        self.x = []
        self.yn = []
        self.fitted_data = []


    def func(self,x, amplitude, frequency,offset,move):

        return amplitude*np.sin(frequency*x + offset) + move

    def getData(self,x,yn):
        self.x = x;
        self.yn = yn;

    def fit(self,guessData):
        try:
            self.popt, pcov = curve_fit(self.func, self.x, self.yn,guessData)
        except:
            print 'Curve_fit Error'
        try:
            self.dataCreator()
        except:
            print 'DataCreator Error'


    def dataCreator(self):
        self.fitted_data = self.func(self.x, self.popt[0], self.popt[1],self.popt[2],self.popt[3])

    def printPopt(self):
        print self.popt
        return self.popt

    def returnPopt(self):
        return self.popt

    def returnFittedData(self):
        return self.fitted_data
