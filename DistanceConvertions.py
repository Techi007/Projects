#DistanceConvertions.py
#Author: Robert S. Soto
#Date: 24 June 2020

def main():
	units = input("Which unit are you using? (INCH for Inches, FEET for feet)")
	distance = eval(input("Please enter the distance: "))
	if (units == 'INCH'):
		inches = distance * 12
		print("The distance is", inches, "Inches.")
	else:
		feet = distance / 12
		print("The distance is", round(feet, 5), "Feet.")