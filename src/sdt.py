import scipy.stats as stats #Statistical package from open-source python library

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    #Calculates the hit rate
    def hits_rate(self):
        return self.hits/(self.hits+self.misses)

    #Calulcates the false alarm rates
    def falseAlarms_rate(self):
        return self.falseAlarms/(self.falseAlarms+self.correctRejections)

    #Calculates d_prime 
    def d_prime(self):
        H = self.hits_rate()
        FA = self.falseAlarms_rate()

        #Calculates extreme/perfect scenarios
        if H == 1: #d' for perfect hit rates
            return float('inf')
        if FA == 1: #d' for perfect false alarm rates
            return float("-inf")
        if H == 0 and FA == 0:
            return float("-inf") #d' for worst detection rates

        #Calculates z-scores of hit and false alarm rates using percent point function (inverse of the cumulative distribution function)
        z_H = stats.norm.ppf(H)
        z_FA = stats.norm.ppf(FA) 
        return z_H - z_FA

    #Calculates the criterion (C)
    def criterion(self):
        H = self.hits_rate()
        FA = self.falseAlarms_rate()
       
       ##Calculates extreme/perfect scenarios
        if H ==1 and FA == 0: #Perfect hit rates, no bias
            return 0
        if H == 0 and FA == 1: #Perfect miss, no bias
            return 0
        if H == 0 and FA == 0: #Worst case, no bias 
            return 0
        
        #Calculates z-scores of hit and false alarm rates using percent point function (inverse of the cumulative distribution function)
        z_H = stats.norm.ppf(H)
        z_FA = stats.norm.ppf(FA)
        return-0.5 * (z_H + z_FA)