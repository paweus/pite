import numpy as np
from scipy import stats
class Stats:
    @staticmethod
    def chi(data1,data2):
         obs = np.array([data1,data2])
         chi2, p, dof, expected = stats.chi2_contingency(obs)
         return chi2
