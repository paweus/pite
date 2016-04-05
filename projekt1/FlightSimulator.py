import csv
from Buffer import Buffer

#Klasa symulujaca samolotu
#W rzeczywistosci tylko zczytuje dane z pliku, przepuszcza je przez buffer
#(kazda z danych jest osobna funkcja, symulujac tak jakby podzespoly samolotu)
#i zapisuje do nowego pliku dane, ktore przeszly przez buffer
class FlightSimulator:

    #Konstruktor, przyjmujacy sciezke do pliku, ktory ma otworzyc
    def __init__(self,path):
        self.filePath = path
        print "Flight initialisation"
        self.reader = csv.reader(open(self.filePath, 'rb'))
        self.writer = csv.writer(open('SimulationOutput.csv', 'wb'))
        flight_initialized = True
        self.buffer = Buffer()

    #Funkcja zapisujaca zbuferowane dane
    def openDataSimulation(self):
        print "Buffering data..."
        self.buffered_line = 0

        for row in self.reader:
            if row[0][0] != '#':
                self.startBuffering(row)
                self.buffered_line = self.buffer.returnBuffered()
                if self.buffer.bufferFlag == True:
                    self.writer.writerow(self.buffered_line)
        print "Buffering done"

    #Funkcja uruchamiajaca pobieranie danych przez buffer
    #argumenty: tablica z danymi
    def startBuffering(self,row):
        self.buffer.getTime(row[0])
        self.buffer.getLatitude(row[1])
        self.buffer.getLongitude(row[2])
        self.buffer.getAltitude(row[3])
        self.buffer.getSpeed(row[4])
        self.buffer.getAcceleration(row[5])
        self.buffer.getRoll(row[6])
        self.buffer.getPitch(row[7])
        self.buffer.getHeading(row[8])
        self.buffer.getDate(row[9])
        self.buffer.getFullTime(row[10])
