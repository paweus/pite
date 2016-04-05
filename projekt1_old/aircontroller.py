#!/usr/bin/python

import threading
import sys
from PyQt4 import QtGui, QtCore
import time
import math
import os
import datetime
import csv

class AirPlane(QtGui.QWidget):

    display_update = QtCore.pyqtSignal() # ADDED
#####################################################
## Inicjalizacja zmiennych
#####################################################
    def __init__(self):
        print "Welcome to airlines"
        self.takeoffSpeed = 40 #m/s
        self.started = False
        self.boost = 0
        self.speed = 0
        self.height = 0
        self.angle = 0
        self.acceleration = 1.44 #m/s^2
        self.timeStart = None
        self.timeStop = 0
        self.speed_p = 0
        self.takeoff = False
        self.distance = 0
        self.timeTakeOFF = 0
        self.distanceRunway = 0
        self.dateNow = None
        super(AirPlane, self).__init__()
 
        self.initUI()

#####################################################
## Interfejs
#####################################################
    def initUI(self):

        newfont = QtGui.QFont("Arial", 8, QtGui.QFont.Bold)

        GUIpanel = QtGui.QLabel('Panel samolotu', self)
        GUIpanel.move(240, 10)
        #####################################################
        GUIinfo = QtGui.QLabel('Status:', self)
        GUIinfo.move(40, 10)
        GUIinfo.setFont(newfont)

        #####################################################
        GUIstatus = QtGui.QLabel('Status lotu:', self)
        GUIstatus.move(20, 30)

        self.GUIstatus_value = QtGui.QLabel(self)
        self.GUIstatus_value.setFont(newfont)
        self.GUIstatus_value.move(120, 30)
        self.GUIstatus_value.setText('Nie wystartowal')
        #####################################################
        GUIflightData = QtGui.QLabel('Data wylotu:', self)
        GUIflightData.move(20, 45)

        self.GUIflightData_value = QtGui.QLabel(self)
        self.GUIflightData_value.setFont(newfont)
        self.GUIflightData_value.move(120, 45)
        self.GUIflightData_value.setText('---')
        #####################################################
        GUIflightTime = QtGui.QLabel('Czas lotu:', self)
        GUIflightTime.move(20, 60)

        self.GUIflightTime_value = QtGui.QLabel(self)
        self.GUIflightTime_value.setFont(newfont)
        self.GUIflightTime_value.move(120, 60)
        self.GUIflightTime_value.setText('---')
        #####################################################
        self.GUIparameters = QtGui.QLabel('Parametry:', self)
        self.GUIparameters.move(40, 80)
        self.GUIparameters.setFont(newfont)
        #####################################################
        GUIspeed = QtGui.QLabel('Predkosc:', self)
        GUIspeed.move(20, 100)

        self.GUIspeed_value = QtGui.QLabel(self)
        self.GUIspeed_value.setFont(newfont)
        self.GUIspeed_value.move(120, 100)
        self.GUIspeed_value.setText('---')

        self.GUIspeedkm_value = QtGui.QLabel(self)
        self.GUIspeedkm_value.setFont(newfont)
        self.GUIspeedkm_value.move(120, 115)
        self.GUIspeedkm_value.setText('---')
        #####################################################
        GUIdistance = QtGui.QLabel('Przebyty dystans:', self)
        GUIdistance.move(20, 130)

        self.GUIdistance_value = QtGui.QLabel(self)
        self.GUIdistance_value.setFont(newfont)
        self.GUIdistance_value.move(120, 130)
        self.GUIdistance_value.setText('---')
        #####################################################
        GUIrunway = QtGui.QLabel('Dystans na pasie:', self)
        GUIrunway.move(20, 145)

        self.GUIrunway_value = QtGui.QLabel(self)
        self.GUIrunway_value.setFont(newfont)
        self.GUIrunway_value.move(120, 145)
        self.GUIrunway_value.setText('---')
        #####################################################
        GUIheight = QtGui.QLabel('Wysokosc:', self)
        GUIheight.move(20, 160)

        self.GUIheight_value = QtGui.QLabel(self)
        self.GUIheight_value.setFont(newfont)
        self.GUIheight_value.move(120, 160)
        self.GUIheight_value.setText('---')
        #####################################################
        GUIangle = QtGui.QLabel('Nachylenie:', self)
        GUIangle.move(20, 175)

        self.GUIangle_value = QtGui.QLabel(self)
        self.GUIangle_value.setFont(newfont)
        self.GUIangle_value.move(120, 175)
        self.GUIangle_value.setText('---')
        #####################################################
        GUIacceleration = QtGui.QLabel('Przyspieszenie:', self)
        GUIacceleration.move(20, 190)

        self.GUIacceleration_value = QtGui.QLabel(self)
        self.GUIacceleration_value.setFont(newfont)
        self.GUIacceleration_value.move(120, 190)
        self.GUIacceleration_value.setText('---')

        self.start_button = QtGui.QPushButton("Startuj lot", self)
        self.start_button.clicked.connect(self.initiateFlight)
        self.start_button.move(240, 50)

        self.cancel_button = QtGui.QPushButton("Wylacz system",self)
        self.cancel_button.clicked.connect(self.cancelTracking)
        self.cancel_button.move(240,90)
        self.cancel_button.setEnabled(False)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Samolot')
        self.display_update.connect(self.guiUpdate) # ADDED
        self.show()

#####################################################
## Funkcja odswiezajaca gui
#####################################################
    def guiUpdate(self):
        self.GUIflightTime_value.setText(str(int(self.getTime())) + ' s')
        self.GUIflightTime_value.adjustSize()
        self.GUIspeed_value.setText(str(round(self.speed,1)) + ' m/s')
        self.GUIspeed_value.adjustSize()
        self.GUIspeedkm_value.setText(str(round(self.speed*3.6,1)) + ' km/h')
        self.GUIspeedkm_value.adjustSize()
        self.GUIdistance_value.setText(str(round(self.distance,1)) + ' m')
        self.GUIdistance_value.adjustSize()
        self.GUIrunway_value.setText(str(round(self.distanceRunway,1)) + ' m')
        self.GUIrunway_value.adjustSize()
        self.GUIflightData_value.setText(str(self.dateNow.strftime("%Y-%m-%d %H:%M")))
        self.GUIflightData_value.adjustSize()
        self.GUIangle_value.setText(str(self.angle) + ' deg')
        self.GUIangle_value.adjustSize()
        self.GUIheight_value.setText(str(round(self.height,1)) + ' m')
        self.GUIheight_value.adjustSize()
        self.GUIacceleration_value.setText(str(self.acceleration) + ' m/s^2')
        self.GUIacceleration_value.adjustSize()
        if self.takeoff == False:
            self.GUIstatus_value.setText('Na pasie')
        if self.takeoff == True:
            self.GUIstatus_value.setText('W powietrzu')


#####################################################
## Funkcja odswiezajace informacje o samolocie
#####################################################
    def update(self,stop_event):
            while True and not stop_event.isSet():
                self.updateSpeed()
                self.updateDistance()
                self.printLogs()
                self.saveCSV()
                self.display_update.emit() # ADDED
                if self.takeoff == False:
                    self.ifTakeOFF()
                if self.takeoff == True:
                    self.FlightMode()
                time.sleep(1)

#####################################################
## Funkcja zapisujaca dane do pliku .CSV
#####################################################
    def saveCSV(self):
        writer = csv.writer(self.target)
        writer.writerow((round(self.getTime(),3),round(self.speed,2), round(self.height,3),round(self.angle,2),round(self.acceleration,3),round(self.distance,3),round(self.distanceRunway,3)))

# Funkcja wpisujaca naglowek do pliku z data lotu
    def initlialWrite(self):
        self.target.write("###")
        self.target.write("Date:")
        self.target.write(str(self.dateNow.strftime("%Y-%m-%d %H:%M")))
        self.target.write("\n")


#####################################################
## Funkcja inicjalizacja poczatek lotu
#####################################################

    def initiateFlight(self):
        self.start_button.setEnabled(False)
        self.cancel_button.setEnabled(True)
        self.target = open('log.csv', 'wt')
        self.planeStart()
        #Threading
        self.stop_event = threading.Event()
        self.c_thread = threading.Thread(target = self.update, args=(self.stop_event,))
        self.c_thread.start()

## Funkcja konczaca sledzenie
    def cancelTracking(self):
        #Threading
        self.stop_event.set()
        self.planeStop()
        self.target.close()
        self.close()

# Funkcja inicjalizujaca parametry startowe takie jak czas startu, data
    def planeStart(self):
        self.timeStart = time.time()
        self.started = True
        self.dateNow = datetime.datetime.now()
        self.initlialWrite()

# Dlugosc lotu samolotu
    def planeStop(self):
        self.dateEnd = datetime.datetime.now()
        self.timeStop = time.time()

# Funkcja sprawdzajaca czy samolot oderwal sie od pasa startowego
# Na podstawie sprawdzania czy osiagnal predkosc wymagana do oderwania od ziemi
    def ifTakeOFF(self):
        if self.speed > self.takeoffSpeed:
            if self.takeoff == False:
                print "Samolot wystartowal"
                self.timeTakeOFF = time.time()
            self.takeoff = True

# Aktualizacja predkosci
    def updateSpeed(self):
        if self.speed*3.6 < 900:
            self.speed = self.speed_p + self.acceleration*self.getTime()

#Aktualizacja odleglosci
    def updateDistance(self):
        if self.takeoff == False:
            self.distanceRunway = (self.acceleration*self.getTime()*self.getTime())/2
        else:
            self.distance = self.speed*math.cos(math.radians(self.angle))*self.getTimeTakeoff()

# Zmiana kata przy wznoszeniu i wyrownywaniu
    def FlightMode(self):
        if (self.height < 2000) & (self.angle < 40):
            self.angle += 0.1
            self.height += self.speed*math.sin(math.radians(self.angle))
        if (self.height > 2000) & (self.angle > 0):
            self.angle -= 0.3
            self.height += self.speed*math.sin(math.radians(self.angle))
        if(self.angle <= 0):
            self.angle = 0

# Zwraca czas w sekundach od poczatku lotu
    def getTime(self):
        return time.time() - self.timeStart + self.boost

# Zwraca czas w sekundach od oderwania sie od ziemi
    def getTimeTakeoff(self):
        return time.time() - self.timeTakeOFF

# Drukuje logi w konsoli
    def printLogs(self):
        print '-------------------'
        print 'Czas',self.getTime()
        print 'Speed ',self.speed * 3.6,"km/h   //  ",self.speed,"m/s"
        print 'Dystans', self.distance
        print 'Dystans na pasie', self.distanceRunway
        print 'Wysokosc ',self.height
        print 'Kat wznoszenia',self.angle


def main():

    app = QtGui.QApplication(sys.argv)
    ex = AirPlane()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
