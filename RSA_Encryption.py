# encoding: utf-8

#Found phiden with p and q
def nphiden(p, q):
	n = p * q
	print("\nn = ", n)
	phiden = (p - 1) * (q - 1)
	return (n, phiden)

#Found pgcd with a and b
def pgcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;

#Found e with p, q and phiden
def founde(p, q, phiden):
	compteur = 0
	PGCD1 = 0
	e = 0
	while PGCD1 != 1 :
		while compteur == 0 :
			if((p < e) and (q < e) and (e < phiden)):
				compteur = 1
			e = e + 1
		PGCD1 = pgcd(e, phiden)
	return e

#check if integer n is a prime
def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i += 2
    return True

# ask the user for p and q
def askpq():
	i = False
	while i == False:
		try:
			p = int(input('Enter prime number p: '))
			q = int(input('Enter prime number q: '))
			if isprime(p) == True and isprime(q) == True:
				i = True
			else:
				print("Please enter 2 prime numbers\n")
		except ValueError:
			print("Please enter a number\n")
	return p, q

#Function to found d
def foundd(e, phiden, p, q):
	d = 0
	i = 0
	while i == 0:
		if ((e * d % phiden == 1) and (p < d) and (q < d) and (d < phiden)):
			i = 1
		d = d + 1
	d = d - 1
	return d

#Create and show the public key
def publickey():
	p, q = askpq()
	n, phiden = nphiden(p, q)
	print("phi of n = ", phiden)
	e = founde(p, q, phiden)
	print("Public key (", e, ",", n, ")")
	d = foundd(e, phiden, p, q)
	print("Private key(", d, ",", n, ")")
	return p, q, n, phiden, e

#Encrypt the string passed in parameter
def encryp_string(string, n, phiden, e):
	string_size = len(string)
	i = 0
	print("\nEncrypted string = ", end='')
	while i < string_size:
		ascii = ord(string[i])
		crypt_letter = pow(ascii, e) % n
		if ascii > n:
		    print("p and q are too small, please restart.\n")
		if crypt_letter > phiden:
			print("Math error\n")
		print(crypt_letter, end = ' ')
		i = i + 1
	print()

#Function for the encryption program
def encryption():
	#Public Key
	p, q, n, phiden, e = publickey()
	# Encryption
	string = input('Enter the string to encrypt: ')
	encryp_string(string, n, phiden, e)

#Factoring function to found p, q and phiden
def factoring(n):
	b = 2
	while b:
		while n % b!=0:
			b =  b + 1
		if n / b == 1:
			p = b
			break
		q = b
		n = n / b;
	phiden = (p - 1) * (q - 1)
	print()
	return p, q, phiden

#Function to found p and q from d
def hackpq():
	i = 0
	while i == 0:
		try:
			d = int(input('Enter number d: '))
			n = int(input('Enter the number n: '))
			i = 1
		except ValueError:
			print("Please enter a number\n")
	p, q, phiden = factoring(n)
	i = 0
	print("Private key (",d,",",n,")\n")
	return d, n

#Function to ask d value
def askd():
	i = False
	while i == False:
		try:
			d = int(input('d value: '))
			i = True
		except ValueError:
			print("\nPlease enter a number\n")
			i = False
	print()
	return d

#Operation of decipherment on the word
def word_decipherment(d, n, word):
	ascii = (pow(word, d) % n)
	print(chr(ascii), end='')

#Take the string and apply decipherment on each word
def string_decipherment(d, n):
	i = False
	while i == False:
		try:
			string = input('Enter the encrypted string: ')
			i = True
		except ValueError:
			print("\nPlease enter a string\n")
			i = False
	i = 0
	length = len(string)
	word = ""
	try:
		while i < length - 1:
			while i < length and string[i] != ' ':
				word = word + string[i]
				i = i + 1
			word_decipherment(d, n, int(word))
			i = i + 1
			word = ""
	except:
		print("Wrong string value", end = "")
	print("\n")

#Main function for decipherment
def main_decipherment():
	d, n = hackpq()
	string_decipherment(d, n)

# Main loop
if __name__ == "__main__":
        i = -1
        while i != 0:
                try:
                	i = int(input('1: Encryption\n2: Decipherment\n0: Exit\nYour choice: '))
                except ValueError:
                	print("\nPlease enter a number")
                print()
                if i == 1:
                        encryption()
                elif i == 2:
                        main_decipherment()
