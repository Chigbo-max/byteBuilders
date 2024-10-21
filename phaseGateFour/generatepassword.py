import string
import random

def generate_password():
	array = [ ]
	
	for characters in range(random.randrange(16, 80)):
		password = random.choice(string.printable).strip()
		if password: 
			array.append(password)
	return ''.join(array)

print(generate_password())
	


