# Name: Charlotte Moreland
# Date: 4/28/23
# Assignment: CS 333 Final Project
# Filename: testing.py

import unittest
from account import Account
from customer import Customer
from admin import Admin
from transaction import Transaction
from atm import ATM

class TestAccount(unittest.TestCase):

  def setUp(self):
    self.account = Account(1000)

  def test_deposit(self):
    self.assertEqual(self.account.deposit(100), 100, "Deposit added correctly")

  def test_withdraw(self):
    self.account.balance = 200
    self.assertEqual(self.account.withdraw(100), 100, "Withdrawal should work")
    self.assertIsNone(self.account.withdraw(300), "Withdrawal should not go through")

  def test_checkBalance(self):
    self.account.balance = 200
    self.assertEqual(self.account.checkBalance(), 200, "Check balance should go through")

class TestAdmin(unittest.TestCase):

  def setUp(self):
    self.admin = Admin()
    self.admin2 = Admin()
    self.realCustomer = self.admin2.addCustomer("Jill", "12 Salmon Lane", "654-876-9876")
  
  def test_addCustomer(self):
    customer2 = self.admin.addCustomer("Bob", "123 1st St", "555-888-5757")
    self.assertEqual(customer2.name, "Bob", "Customer should be named Bob")
    self.assertEqual(customer2.address, "123 1st St", "Address should match")
    self.assertEqual(customer2.phone, "555-888-5757", "Phone should match")

  def test_removeCustomer(self):
    self.customer1 = self.admin.addCustomer("Nate", "345 3rd St", "555-530-1039")
    self.admin.addCustomer("Bob","123 1st St", "555-888-5757")
    self.admin.removeCustomer(self.customer1)
    self.assertEqual(self.admin.customers[0].name, "Bob", "1st customer name should be removed")
    self.assertEqual(self.admin.customers[0].address, "123 1st St", "1st customer address should be removed")
    self.assertEqual(self.admin.customers[0].phone, "555-888-5757", "1st customer phone should be removed")

  def test_getCustomerByName_customerExists(self):
    self.assertEqual(self.admin2.getCustomerByName("Jill"), self.realCustomer, "Customer should exist")
    
  def test_getCustomerByName_customerNotExists(self):
    self.assertIsNone(self.admin2.getCustomerByName("Bill"), "Customer should not exist")

class TestATM(unittest.TestCase):

  def setUp(self):
    self.atm = ATM(1000)

  def test_updateCash(self):
    self.assertEqual(self.atm.updateCash(200), 1200, "Cash should be updated")

  def test_checkCash(self):
    atm2 = ATM(1000)
    self.assertEqual(atm2.checkCash(), 1000)

class TestCustomer(unittest.TestCase):

  def setUp(self):
    self.customer = Customer("Steve", "123 Firefly", "800-838-8585")
    self.customer2 = Customer("Kevin", "123 Sky", "830-838-8585")
    self.customer3 = Customer("Valerie", "555 Tagus Ct", "830-432-5475")
    self.account2 = self.customer2.openAccount(333)
    self.account3 = self.customer3.openAccount(555)

  def test_openAccount_accountAppended(self):
    self.customer.openAccount(1234)
    self.assertEqual(self.customer.accounts[0].accountNum, 1234, "account number should match")
    
  def test_closeAccount(self):
    self.customer2.closeAccount(self.account2)
    self.assertNotIn(self.account2, self.customer2.accounts, "Account should not exist")

  def test_accountExists_DoesExist(self):
    self.assertEqual(self.customer3.accountExists(555), self.account3, "Accounts should Match")

  def test_accountExists_DoesNotExist(self):
    self.assertIsNone(self.customer3.accountExists(242), "Account should not exist")
    
class IntegrationTests(unittest.TestCase):
  
  def test_deposit_transactionHistory(self):
    account = Account(1000)
    account.deposit(100)
    self.assertEqual(account.transactionHistory[0].amount, Transaction("deposit", 100).amount, "Transaction should be saved")

  def test_withdraw_transactionHistory(self):
    account = Account(1000)
    account.balance = 500
    account.withdraw(300)
    self.assertEqual(account.transactionHistory[0].amount, Transaction("withdraw", 300).amount, "Transaction should be saved")

  def test_dispenseCash_cashAvailable(self):
    atm = ATM(10000)
    account = Account(1234)
    account.deposit(600)
    self.assertTrue(atm.dispenseCash(account, 500), "Cash should dispense from ATM")

  def test_dispenseCash_NotEnoughInAtmOrAccount(self):
    atm = ATM(10000)
    atm2 = ATM(100)
    account = Account(1234)
    account.deposit(600)
    self.assertFalse(atm.dispenseCash(account, 11000), "There should be not enough cash in ATM or account")

  def test_dispenseCash_NotEnoughInAtm(self):
    atm2 = ATM(100)
    account = Account(1234)
    account.deposit(600)
    self.assertFalse(atm2.dispenseCash(account, 500), "There should be not enough cash in ATM")

  def test_dispenseCash_NotEnoughInAccount(self):
    atm = ATM(10000)
    account = Account(1234)
    account.deposit(600)
    self.assertFalse(atm.dispenseCash(account, 700), "There should be not enough cash in account")
    
if __name__ == "__main__":
  unittest.main()