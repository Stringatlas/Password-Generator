import random
import string
import generate
class Generator:
	adjectives = ["red", "orange", "yellow", "green", "blue", "purple", "brown",
	"sublime", "big", "small", "excellent", "splendid", "supreme", "impressive"]
	nouns = ["Apple", "Pear", "Grape", "Kiwi", "Banana", "Peach", "Corn", "Shark",
		 	"Horse", "Goose", "Duck", "Eagle", "Cow", "Sheep", "Goat", "Trout"]
	symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
	punctuation = string.punctuation
	alphabet = string.ascii_lowercase
	digits = string.digits

	def generate_password(security=0, required="", min=0, max=0, capital=0, symbol=0):
		if security == 0:
			if len(required) > max and max != 0:
				return "Invalid arguments: Length of required characters is less than maximum password length"
			symbols = random.choice(Generator.symbols) * symbol
			numbers = str(random.choice([1, 2, 3, 4, 5, 7, 8, 9])) * 3
			noun = random.choice(Generator.nouns)
			adj = random.choice(Generator.adjectives)
			extra = ""
			password = adj + noun + numbers + symbols
			if min > 0:
				a = min - len(password) - len(required)
				password =adj + noun
				while a > 0:
					try:
						extra = random.choice([element for element in Generator.nouns if len(element) < a])
					except:
						break
					password += extra
					a = min - len(password) - 3
				numbers += numbers[0] * (min - len(password) - len(symbols) - len(required) - 3)
				password += required + numbers + symbols
				return password
			else:
				password = adj + noun + required + numbers + symbols
			if len(password) > max and max != 0:
				return password[0:max]
			return password


		if security == 1:
			password = ""
			lengt = max - len(required) - 3

			if max == 0:
				lengt = 16

			if lengt < 0:
				return "I was too lazy to debug this, just increase the maximum please"

			
			length = lengt // 26 if lengt > 26 else 0
			
			lengt = lengt - length * 26 if length >= 1 else lengt
			
			for _ in range(length):
				password += Generator.alphabet

			start = random.randint(0, (26 - lengt))

			letters = ""
			numbers = ""

			for x in range(3):
				numbers += str(random.randint(1, 5))


			letters = Generator.alphabet[start: start + lengt]
			password += letters + numbers
			return password

		if security == 2:
			numbers = ""
			req = required.split()
			symbols = random.choice(Generator.symbols) * symbol

			if max != 0 and (max < (len(req) + len(symbols))):
				return "Invalid arguments: Length of required characters is less than maximum password length"
			elif max == 0:
				length = 50
			elif max < 11:
				length = max - len(req) - len(symbols)
				length = length // 2 + length % 2
			else:
				length = max - len(req) - len(symbols) - 5
			a = max // 2 if length <= 10 else 5

			for x in range(a):
				numbers += str(random.randint(1, 9))
			letters = [random.choice(Generator.alphabet) * random.randint(0, 1) or (random.choice(Generator.alphabet).upper())
					  for _ in range(length)]

 
			password = "".join(letters) + numbers 
			a = ""
			for x in req:
				if x not in password:
					a += x
			return "".join(letters) + a + numbers 



		if security == 3:
			maximum = (65 - len(required)) if max == 0 else max - len(required)

			if maximum < 0:
				return "Invalid arguments: Length of required characters is less than maximum password length"

			if max > 65:
				maximum = max - len(required)

			password = []
			for _ in range(maximum):
				choice = random.randint(0, 3)
				if choice == 0:
					password.append(random.choice(Generator.alphabet)) # lowercase letter
				elif choice == 1:
					password.append(random.choice(Generator.alphabet).upper()) # uppercase letter
				elif choice == 2:
					password.append(str(random.randint(0, 9)))
				else:
					password.append(random.choice(Generator.symbols))
			password = "".join(password)

			uni = [x for x in required.split() if x not in password]

			return password + "".join(uni)



