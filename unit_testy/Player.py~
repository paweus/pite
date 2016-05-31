from Wisielec import Wisielec


class Player:
	#Inicjalizacja 
	def __init__(self):
		print 'Prosta gra w wisielca.'
		while True:
			inp = raw_input('Nacisnij 1, aby rozpoczac gre.\nNacisnij q, aby zakonczyc.\n')
			if(inp == str(1)):
				self.StartGame(Wisielec.GetCode())
			elif(inp == 'q'):
				break

	#rozpoczyna gre, ustawia tablice ze slowem na '_'
	def StartGame(self,Code):
		self.errors = 0
		self.maxerrors = Wisielec.MaxErr(Code)
		self.word = [] 
		self.chars = []
		#print Code
		print 'Twoje slowo:'
		for i in range(len(Code)):
			self.word.append('_')
		print self.word
			
		print 'Popelnione bledy ' + str(self.errors)+' \ '+str(self.maxerrors)
		self.Play(Code)
		
		
	#pobiera literke z klawiatury
	def GetChar(self):
		while True:
			char = raw_input('Podaj dokladnie 1 litere\n')
			if(char in self.chars):
				print 'Podales wczesniej ta litere!'			
				continue
			elif(len(char) == 1 and not char.isdigit()):
				self.chars.append(char)
				return char
	
	#wlasciwa gra,sprawdza warunki przegrania/wygrania, dodaje prawidlowe literki
	def Play(self,Code):
		while(self.errors<self.maxerrors):
			if(Wisielec.IsWinner(self.word,Code)):
				print 'Wygrales! Ukryte slowo to '+Code
				break
			print '*****************************'
			win = Wisielec.CheckChar(self.GetChar(),self.word,Code)
			if(not win):
				self.errors +=1
			print 'Twoje slowo:'
			Wisielec.PrintWord(self.word)
			print 'Popelnione bledy ' + str(self.errors)+' \ '+str(self.maxerrors)
		if(self.errors==self.maxerrors):
			print 'Przegrana! Ukryte slowo to '+Code
		print '****************************************************************************'
		
		

