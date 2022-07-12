#An ATM Machine
#Author: Robert S. Soto

#ATM.py

class Card:
    
    def __init__(self, cardHolder, balance): #string, string, integer
        self.cardHolder = cardHolder
        self.balance = balance

    def deposit(self, addBalance):
        self.balance += addBalance

    def withdraw(self, subsBalance):
        self.balance -= subsBalance

    def balance(self):
        return self.balance
