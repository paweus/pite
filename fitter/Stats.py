import numpy as np
from scipy import stats

#Klas implementujaca test chi2
class Stats:
    #Metoda statyczna implementujaca metode chi2_contingency
    #Argumenty: zestaw danych funkcji poczatkowej, zestaw danych funkcji dopasowanej
    @staticmethod
    def chi(data1,data2):
         obs = np.array([data1,data2])
         try:
             chi2, p, dof, expected = stats.chi2_contingency(obs)
         except:
            print 'Chi2 error'

         return chi2
