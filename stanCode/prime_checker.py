"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


def main():
	"""
	TODO:
	"""
	print("welcome to prime checker")
	n = int(input("n: "))
	a = 2

	while True:
		if n == 1:
			print('fail')
			n = int(input("n: "))
		if n == 2:
			print("n is a prime")
			n = int(input("n: "))

		if n % a != 0:
			a += 1
			print(str(a))
			if n == a:
				print("n is a prime")
				n = int(input("n: "))
				a = 2
		# else:
		# 	print(str(a))
		# 	print("n is not a prime")
		# 	n = int(input("n: "))
		# 	a = 2
		else:
			if n != a:
				print("n is not a prime")
				n = int(input("n: "))
				a = 2

	pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
