import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl

class Plotter:
    poczatkowa = True
    dopasowana = True
    dane = True
    xlim_min = 0
    xlim_max = 10
    def __init__(self):
        self.fig = mpl.figure()

    def plot(self,x,y,yn,fitted_data):
        # Plot out the current state of the data and model
        self.fig.clf()

        ax = self.fig.add_subplot(111)
        if(Plotter.dane):
            ax.scatter(x, yn,c='g',s=10,edgecolor='green',label='Data')
#        fig.savefig('model_and_noise.png')
        if(Plotter.dopasowana):
            ax.plot(x, fitted_data, c='r',linewidth=4.0, label='Best fit')
        if(Plotter.poczatkowa):
            ax.plot(x, y, c='b',linewidth=1.0, label='Function')
        ax.legend(prop={'size':10})
        mpl.xlim((Plotter.xlim_min,Plotter.xlim_max))
#        fig.savefig('model_fit.png')
        #mpl.show()
        return self.fig
