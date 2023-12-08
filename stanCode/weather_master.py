"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -100

def main():
	"""
	TODO:
	"""

	temp1 = int(input("Next temperature: (or -100 to quit?)"))
	a = 0

	if temp1 < 16:
		cold = 1
	else:
		cold = 0


	if temp1 == QUIT:
			print("no data")
	else:
		max = temp1
		min = temp1
		total = temp1
		a += 1

		while True:
			temp2 = int(input("Next temperature: (or -100 to quit?)"))
			total = total + temp2
			a += 1
			if temp2 == QUIT:
				a = a - 1
				avg = (total-QUIT) / a
				print(str(avg))
				break
			else:
				if temp2 > max:
					max = temp2
				else:
					min = temp1
				if temp2 < 16:
					cold += 1

		print("h temp: " + str(max))
		print("m temp: " + str(min))
		print("cold days: " + str(cold))
		# print("avg temp: " + str())







	pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
