#interest.py
#Author: Robert S. Soto
#Date: June 28, 2020

#A program that represents an Interest Generator.

from math import exp
def simpleInterest(P, r, t):
    I = P*r*t #I has local scope
    return I
simpleInterest(100, 0.05, 4)

def compoundInterest(P, r, t, n):
    A = P*(1+r/n)**(n*t)
    I = A - P
    return I

def continuousCompoundInterest(P, r, t):
    A = P*exp(r*t)
    I = A - P
    return I

def main():
    Principal = eval(input("Please enter the amount you wish to invest: "))
    ratePercent = eval(input("Please enter in percent, your rate of interest: "))
    rate = ratePercent / 100
    time = eval(input("Please enter number of years of investment: "))
    kindOfInterest = input("Please let us know the kind of interest you want (S for simple, C for compound, CC for continuous Compound): ")
    
    if kindOfInterest == 'S':
        print(f"Simple interest is ${simpleInterest(Principal, rate, time)}.")
    elif kindOfInterest == 'C':
        print(f"Compound interest compounded monthly is ${compoundInterest(Principal, rate, time, number)}.")
    else:
        print(f"Compound interest compounded continuos is ${continuosCompoundedInterest(Principal, rate, time)}.")

if __name__ == '__main__':
    print("Simple Interest is $%2.2f"%simpleInterest(100, 0.05, 4))
    print("Compound interest compounded monthly is $"+str(round(compoundInterest(100, 0.05, 4, 12), 2)))
    print("Compound interest compounded continous is $"+str(round(continuousCompoundInterest(100, 0.05, 4), 2)))
