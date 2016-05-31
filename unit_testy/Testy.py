import unittest
#Nie wiem jak testowac ten program


from Player import Player

class TestHangMan(unittest.TestCase):
	def setUp(self):


		self.testy = Player()
		# self.testy2 = Player()

	#Czy ilosc popelnionych bledow nie jest wieksza od maksymalnej ilosci bledow
	def test_MaxErrors(self):
		self.assertGreaterEqual(self.testy.maxerrors,self.testy.errors)

	


	# Uruchomienie gry z innym slowem
	# Problematyczne do testowania

	# def test_Code(self):
	# 	self.assertRaises(TypeError, self.testy2.StartGame("test"))



if __name__ == '__main__':
	unittest.main()
