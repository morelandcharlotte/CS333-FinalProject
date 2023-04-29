# Name: Charlotte Moreland
# Date: 4/24/23
# Assignment: CS 333 Final Project
# Filename: atm.py

class ATM:
  
  def __init__(self, availableCash):
    self.availableCash = availableCash

  def dispenseCash(self, account, amount):
    if self.availableCash >= amount and account.balance >= amount:
      account.withdraw(amount)
      self.availableCash -= amount
      return True
    else:
      print("Unable to dispense cash.")
      return False

  def updateCash(self, amount):
    self.availableCash += amount
    return self.availableCash

  def checkCash(self):
    return self.availableCash
    