
import numpy as np

#Klasa generujaca statystyki do GUI
class Statistics:
    def __init__(self,data,data2):
        self.data = data
        self.dataStr = data2
        self.counter = 0
        self.timeFlight = 0

        self.timeStart = 0
        self.timeLand = 0
        self.dateStart = 0
        self.dateLand = 0
        self.maxSpeed = 0
        self.maxAcceleration = 0
        self.maxAltitude = 0
        self.latitudeStart = 0
        self.longitudeStart = 0
        self.latitudeLand = 0
        self.longitudeLand = 0
        self.averageSpeed = 0
        self.averageHeight = 0
        self.startPoint = 0
        self.endPoint = 0

    #Proste generowanie statystyk
    def makeStats(self):
        print 'Generate statistics...'
        self.timeStart = self.dataStr[0,10]
        self.dateStart = self.dataStr[0,9]
        self.latitudeStart = self.data[0,1]
        self.longitudeStart = self.data[0,2]
        self.startPoint = self.data[0,3]
        for row in self.data:
            if(row[3] > self.maxAltitude):
                self.maxAltitude = row[3]
            if(row[4] > self.maxSpeed):
                self.maxSpeed = row[4]
            if(row[5] > self.maxAcceleration):
                self.maxAcceleration = row[5]
            self.counter = self.counter + 1

        #Po forze
        self.timeFlight = self.data[self.counter-1,0]
        self.timeLand = self.dataStr[self.counter-1,10]
        self.dateLand = self.dataStr[self.counter-1,9]
        self.latitudeLand = self.data[self.counter-1,1]
        self.longitudeLand = self.data[self.counter-1,2]
        self.endPoint = self.data[self.counter-1,3]
        self.averageSpeed = np.mean(self.data[:,4])
        self.averageHeight = np.mean(self.data[:,3])
