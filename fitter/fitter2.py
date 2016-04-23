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
        print self.x
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

    def getData(self,x,yn):
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


class Stats:
    @staticmethod
    def chi(data1,data2):
         obs = np.array([data1,data2])
         chi2, p, dof, expected = stats.chi2_contingency(obs)
         print chi2
        # critical = 0.0
        #expected = np.array(data1)
        #observed = np.array(data2)
        # for exp,obs in zip(expected,observed):
        #     xsqr = obs - exp
        #     print xsqr
        #     critical += ((xsqr*xsqr)/exp)
        #chi = np.sum((np.power(np.absolute(observed) - np.absolute(expected),2))/np.absolute(expected))
        #normalized_chi = float(chi)/float(len(observed))
        # print critical
    #    print chi


class Plotter:
    def plot(self,x,y,yn,fitted_data):
        # Plot out the current state of the data and model
        fig = mpl.figure()
        ax = fig.add_subplot(111)
        ax.scatter(x, yn,c='g',s=10,edgecolor='green',label='Data')
#        fig.savefig('model_and_noise.png')
        ax.plot(x, fitted_data, c='r',linewidth=4.0, label='Best fit')
        ax.plot(x, y, c='b',linewidth=1.0, label='Function')
        ax.legend()
        mpl.xlim((0,10))
#        fig.savefig('model_fit.png')
        mpl.show()

class Main:
    #tworzenie generatora
    gen = Generator()
    #uruchamianie kreatora
    gen.creator()
    #tworzenie fittera
    fit = Fitter()
    fit.getData(gen.returnX(),gen.returnYn())
    #fittowanie
    fit.fit()
    #wydrukowanie zfitowanych wartosci
    fit.printPopt()
    #tworzenie plottera
    plot = Plotter()
    #pobieranie danych do plottera
    plot.plot(gen.returnX(),gen.returnY(),gen.returnYn(),fit.returnFittedData())
    Stats.chi(gen.returnY(),fit.returnFittedData())
