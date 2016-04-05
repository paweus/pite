
#Klasa zawierajaca operacje matematyczne, majace na celu zmienic system jednostek na metryczne
class Operations:
    @staticmethod
    def CalculateToMetrics(data):
        print 'Units recalculations...'
        temp = data
        temp = Operations.recalculateFeetsToMeters(temp)
        temp = Operations.recalculateKnotsToKph(temp)
        return temp

    #Funkcja zmieniajaca stopy na metry
    @staticmethod
    def recalculateFeetsToMeters(data):
        for row in data:
            row[3] = row[3]*0.3048
        return data

    #Funkcja zmieniajaca knot na km/h
    @staticmethod
    def recalculateKnotsToKph(data):
        for row in data:
            row[4] = row[4]*1.85
        return data
