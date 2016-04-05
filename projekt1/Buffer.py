# encoding=utf8
from Validator import Validator
import time

# Klasa ktora ma na celu bufferowac dane, w wypadku, gdyby zaistnialo opoznienie w przesyle z samolotu do systemu
# W teorii powinno oczekiwac przez 1 sekunde na nowe, splywajace dane, lecz do przetestowania tego nalezaloby stworzyc
# fikcyjne podzespoly samolotow na wątkach i generowac w nich dane + symulowac opoznienie.
# Wtedy naplewajace dane gromadzone bylyby w tablicach i po odblokowaniu zatoru wysylane dalej
#
# W praktyce dziala to tak, ze jesli w pliku CSV brakuje jakiejs danej to program czeka 1 sekunde (10 prob) na to, zeby brakujace dane sie pojawily
# Oczywiscie nie moze się to stac, wiec po 10 probach porzuca niekompletna linijke i idzie dalej

class Buffer:
    def __init__(self):
        print '---------------------------'
        print 'Buffer opened'
        self.time = []
        self.latitude = []
        self.longitude = []
        self.altitude = []
        self.speed = []
        self.acceleration = []
        self.pitch = []
        self.roll = []
        self.heading = []
        self.date = []
        self.fullTime = []
        self.bufferedData = []
        self.bufferFlag = True

    #Funkcja, w ktorej wszystkie otrzymane wartosci zapisywane sa do jednej talicy.
    #Tablica jest walidowana, pod katem poprawnosci zawartych danych.
    #Jezeli tablica przejdzie walidacje to wszystkie zbuferowane juz wartosci sa usuwane ze zmiennych, a sama tablica jest wysylana dalej do zapisuje
    #Jezeli tablica nie przejdzie walidacji to nastepuje oczekiwanie (max 10 razy) na to, aby dane dotarly
    #W przeciwnym razie linijka jest porzucana
    def returnBuffered(self):
        self.deepCounter = 0
        while self.deepCounter < 10:
            self.bufferedData = [self.time[0],self.latitude[0],self.longitude[0],self.altitude[0],self.speed[0],self.acceleration[0],self.roll[0],self.pitch[0],self.heading[0],self.date[0],self.fullTime[0]]
            if Validator.validate(self.bufferedData):
                self.popFirstIndex()
                self.bufferFlag = True
                return self.bufferedData
            time.sleep(0.1)
            self.deepCounter += 1
        self.bufferFlag = False
        self.popFirstIndex()
        print 'Skipping line'

        return 0

    #Funkcja usuwajaca dane z poczatku tabeli(tj index 0) dla wszystkich danych
    def popFirstIndex(self):
        self.nullWard(self.time)
        self.nullWard(self.latitude)
        self.nullWard(self.longitude)
        self.nullWard(self.altitude)
        self.nullWard(self.speed)
        self.nullWard(self.acceleration)
        self.nullWard(self.roll)
        self.nullWard(self.pitch)
        self.nullWard(self.heading)
        self.nullWard(self.date)
        self.nullWard(self.fullTime)

    #Funkcja pomocnicza, ktora wyrzuca pierwszy element z listy
    def nullWard(self,data):
        if data[0] == '':
            data[0] = '0'
        data.pop()[0]

    #Funkcje pobierajace dane i zapisujace do nowych zmiennych, odpowiadajacych ich typowi
    def getTime(self,data):
        if data is not None or "":
            self.time.append(data)

    def getLatitude(self,data):
        if data is not None or "":
            self.latitude.append(data)

    def getLongitude(self,data):
        if data is not None or "":
            self.longitude.append(data)

    def getAltitude(self,data):
        if data is not None or "":
            self.altitude.append(data)

    def getSpeed(self,data):
        if data is not None or "":
            self.speed.append(data)

    def getAcceleration(self,data):
        if data is not None or "":
            self.acceleration.append(data)
        else:
             self.acceleration.append('')

    def getPitch(self,data):
        if data is not None or "":
            self.pitch.append(data)

    def getRoll(self,data):
        if data is not None or "":
            self.roll.append(data)

    def getHeading(self,data):
        if data is not None or "":
            self.heading.append(data)

    def getDate(self,data):
        if data is not None or "":
            self.date.append(data)

    def getFullTime(self,data):
        if data is not None or "":
            self.fullTime.append(data)
