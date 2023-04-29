# Name: Charlotte Moreland
# Date: 4/24/23
# Assignment: CS 333 Final Project
# Filename: account.py

from transaction import Transaction

class Account:

  def __init__(self, accountNum):
    self.accountNum = accountNum
    self.balance = 0
    self.transactionHistory = []

  def deposit(self, amount):
    self.balance += amount
    self.transactionHistory.append(Transaction("deposit", amount))
    return self.balance

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      self.transactionHistory.append(Transaction("withdrawal", amount))
      return self.balance
    else:
      print("Insufficient funds.")
      return None

  def checkBalance(self):
    return self.balance

  def viewTransactions(self):
    for transaction in self.transactionHistory:
      print("Transaction Type: " + transaction.type + ", Transaction Amount: " + str(transaction.amount))
