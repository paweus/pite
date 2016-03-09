#!/usr/bin/env python

# Tablica globalna przechowywujaca rownania (w postaci tablic) 
equations = []


# InputValidator odpowiada za sprawdzanie poprawnosci wprowadzonych danych
# Posiada jedna funkcje statyczna, ktora sprawdza czy wartosc jest poprawna
# w przeciwnym razie zwraca informacje o blednej wprowadzonej wartosci (co wymusza ponowne jej podanie w klasie InputReader)
class InputValidator:
	@staticmethod
	def CheckIfIsInt(value):
		if value is None:
			return 1
		else:
			try:
				val = int(value)
			except ValueError:
				print("Podana liczba nie jest liczba, wprowadz ponownie poprawna wartosc.")
				return 1
		return 0

# InputReader odpowiada za przyjmowanie danych przez uzytkownika
# Dane sa walidowane przy pomocy metody z klasy InputValidator
# Klasa posiada licznik wprowadzonych rownan (lecz program jest przygotowany na 2 rownania)
# Jezeli dane sa poprawne zapisywane sa do tablicy, po zrzutowaniu na int
# Klasa posiada dodatkowo takze metode sluzaca jako getter wartosci dla podanego ID w tablicy
class InputReader:
	equationsCounter = 0
	def __init__(self):
		InputReader.equationsCounter += 1
		self.newEquation = []
		a,b,c, = None, None, None

		print "Wprowadz wartosci a,b,c dla ",InputReader.equationsCounter," rownania, w postaci: "
		print "ax + bx = c"
		print "--------------------"

		# Walidacja w petli while kazdej z wartosci
		# Walidacja przebiega do skutku, do podania prawidlowej wartosci
		while InputValidator.CheckIfIsInt(a):
			a = raw_input('Podaj wartosc a \n')
		while InputValidator.CheckIfIsInt(b):
			b = raw_input('Podaj wartosc b \n')
		while InputValidator.CheckIfIsInt(c):
			c = raw_input('Podaj wartosc c \n')

		# Dodawanie wartosci do tablicy
		self.newEquation.append(int(a))
		self.newEquation.append(int(b))
		self.newEquation.append(int(c))

		print "--------------------"

	# Getter
	def getEquationValue(self,id):
		return self.newEquation[id]


# Solver odpowiada za obliczanie ukladu rownan metoda wyznacznikow
class Solver:
	def __init__(self,equationInput):
		self.equationsHolder = equationInput

# Metoda liczaca wyznaczniki W, Wx, Wy
# Zasada dzialania opisana tutaj: http://matematyka.pisz.pl/strona/1192.html
	def calculateDeterminant(self):
		w = self.equationsHolder[0].getEquationValue(0) * self.equationsHolder[1].getEquationValue(1) - self.equationsHolder[0].getEquationValue(1) * self.equationsHolder[1].getEquationValue(0)
		wx = self.equationsHolder[0].getEquationValue(2) * self.equationsHolder[1].getEquationValue(1) - self.equationsHolder[0].getEquationValue(1) * self.equationsHolder[1].getEquationValue(2)
		wy = self.equationsHolder[0].getEquationValue(0) * self.equationsHolder[1].getEquationValue(2) - self.equationsHolder[0].getEquationValue(2) * self.equationsHolder[1].getEquationValue(0)

		# Obliczanie wynikow
		out = self.calculateResults(w,wx,wy)
		# Wypisywanie wynikow
		self.printResults(out)

# Metoda sprawdzajaca czy uklad ma rozwiazania
# Oblicza rozwiazania lub zwraca stosowny komunikat o rezultacie obliczen
	def calculateResults(self,w,wx,wy):
		if w == 0 & wx == 0 & wy == 0 :
			print 'Uklad nieoznaczony (nieskonczona liczba rozwiazan)'
			return 0
		if w == 0 & wx != 0 & wy != 0:
			print 'Uklad sprzeczny(brak rozwiazan)'
			return 0
		else:
			x = wx/float(w)
			y = wy/float(w)
			results = [x,y]
			return results

# Metoda wypisujaca wyniki
	def printResults(self,results):
		print "Obliczany uklad rownan:"
		for i in range(0,2):
			print  str(self.equationsHolder[i].getEquationValue(0)) + "x " + self.sign(i,1) + " " +str(self.equationsHolder[i].getEquationValue(1)) + "y = " + str(self.equationsHolder[i].getEquationValue(2))
		# Jezeli wynik wynosi 0 oznacza to, ze uklad nie ma jednego rozwiazania
		if(results != 0):
			print "Rozwiazanie: " + str(results)

# Metoda ustalajaca znak przy wypisywaniu obliczanego ukladu rownan.
# W przypadku minusa nie nalezy go wypisywac, gdyz sam jest stawiony razem z liczba
	def sign(self,id,number):
		if self.equationsHolder[id].getEquationValue(number) >= 0:
			return "+"
		else:
			return ""


# ApplicationMgr, klasa glowna, startujaca dzialanie programu z konstruktora.
class ApplicationMgr:
	def __init__(self):

		print  "Program ma za zadanie liczyc uklad 2 rownan liniowych metoda wyznacznikow"
		print "--------------------"
		# Nowe rownania tworzone sa i zapisywane do globalnej tablicy przechowywujacej rownania
		equations.append(InputReader())
		equations.append(InputReader())

		solverObject = Solver(equations)
		solverObject.calculateDeterminant()

		print "--------------------"

# Uruchamianie programu
ApplicationMgr()
