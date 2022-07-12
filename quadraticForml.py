#quadraticForml.py
#Author: Robert S. Soto
#Date: 24 June 2020
from math import sqrt
def main():
	a,b,c = eval(input("Please enter values for a,b,c with commas in between: "))
	if (b**2 - 4*a*c < 0):
		print("We cannot calculate with these inputs.")
	elif (a == 0):
		print("You gave leading coefficient to be 0. Not able to use Quadratic Formula.")
	else:
		solution1 = (-b-sqrt(b**2 - 4*a*c) / (2*a))
		solution2 = (-b+sqrt(b**2 - 4*a*c) / (2*a))
		print("Your solutions:")
		print()
		print(solution1)
		print(solution2)