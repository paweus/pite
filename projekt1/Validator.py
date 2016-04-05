#Klasa walidujaca poprawnosc bufferowanych linijek
class Validator:
    names = ['time','latitude','longitude','latitude','speed','acceleration','roll','pitch','heading','date','full time']

    #Funkcja, ktora sprawdza wszystkie elementy zawarte w tablicy, zbuferowanej przez buffer.
    #Jezeli jakas wartosc jest pustym stringiem to zwracany jest False, co wiaze sie z oczekiwaniem na brakujacy element w buferze
    @staticmethod
    def validate(data):
        counter = 0
        for row in data:
            if row == '':
                #Wypisuje do konsoli na jaka wartosci oczekujemy
                print "Waiting for " + Validator.names[counter]
                return False
            counter += 1
        return True
