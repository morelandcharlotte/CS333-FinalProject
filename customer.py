# Name: Charlotte Moreland
# Date: 4/24/23
# Assignment: CS 333 Final Project
# Filename: customer.py

from account import Account

class Customer:
  
  def __init__(self, name, address, phone):
    self.name = name
    self.address = address
    self.phone = phone
    self.accounts = []

  def openAccount(self, accountNum):
    account = Account(accountNum)
    self.accounts.append(account)
    return account

  def closeAccount(self, account):
    self.accounts.remove(account)

  def viewAccounts(self):
    for account in self.accounts:
      print(" - " + str(self.accounts.index(account) + 1) + " - ")
      print("Account Number: " + str(account.accountNum))
      print("Account balance: " + str(account.balance))

  def accountExists(self, accountNum):
    for account in self.accounts:
      if int(account.accountNum) == int(accountNum):
        return account
        break
    return None

  def viewAccountHistory(self, accountNum):
    account = self.accountExists(accountNum)
    if account != None:
      account.viewTransactions
    else:
      print("Account does not exist")
        
