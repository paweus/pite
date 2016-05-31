import random

codes = ['drzwi','lampa','pies','kot','papuga','krakow','warszawa','programowanie','lizak','rozentuzjazmowany','administrator']

class Wisielec:

	#zwraca haslo
	@staticmethod
	def GetCode():
		global codes
		randd = random.randint(0,len(codes)-1)
		return codes[randd]

	#sprawdza czy literka jest w hasle,jesli tak wstawaia ja/je w odpowiednim miejscu
	@staticmethod
	def CheckChar(char,word,code):
		if(char not in code):
			return False
		else:
			letters = [pos for pos, c in enumerate(code) if c == char]
			for i in range(len(letters)):
				word[letters[i]] = char
			return True
	#ustawianie il bledow w zaleznosci od dl slowa(slabe)
	@staticmethod
	def MaxErr(code):
		if (len(code)<=4):
			return 3
		elif(len(code)>4 and len(code)<=7):
			return 5
		elif(len(code)>7 and len(code)<=13):
			return 7
		else:
			return 10
	#print 
	@staticmethod
	def PrintWord(word):
		print word
	
	#sprawdza czy odgadnieto slowo
	@staticmethod
	def IsWinner(word,code):
		for i in range(len(code)):
			if(word[i] == code[i]):
				tmp = True
			else:
				tmp = False
				break
		return tmp
				
