# Name: Charlotte Moreland
# Date: 4/24/23
# Assignment: CS 333 Final Project
# Filename: main.py

from admin import Admin
from atm import ATM
import random

def main():
  
  admin = Admin()
  atm = ATM(10000)
    
  while True:
    print("\n1. Login as Customer")
    print("2. Login as Bank Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")
        
    if choice == "1":
      # Login as customer
      name = input("Enter your name: ")
      customer = admin.getCustomerByName(name)
            
      if customer is None:
        print("Customer not found.")
            
      else:
        print("Welcome,", customer.name)
        
        while True:
          print("\n1. Deposit")
          print("2. Withdraw")
          print("3. Check Balance")
          print("4. View Transactions")
          print("5. Open Account")
          print("6. Close Account")
          print("7. Back")
          choice = input("Enter your choice: ")
                
          if choice == "1":
            # Deposit
            if(len(customer.accounts) == 0):
              print("Please create an account before proceeding")
            else:
              accountNum = input("Please enter the number for the account you which to deposit money to: ")
              account = customer.accountExists(accountNum)
              if account == None:
                print("Account does not exist")
              else:
                amount = float(input("\nEnter amount to deposit: "))
                account.deposit(amount)
                print("Deposit successful.")
                    
          elif choice == "2":
            # Withdraw
            if(len(customer.accounts) == 0):
              print("Please create an account before proceeding")
            else:
              accountNum = input("Please enter the number for the account you would like to withdraw money from: ")
              account = customer.accountExists(accountNum)
              if account == None:
                print("Account does not exist")
              else:
                amount = float(input("\nEnter amount to withdraw: "))
                account.withdraw(amount)
                print("Withdrawal successful.")
                    
          elif choice == "3":
            # Check balance
            accountNum = input("Please enter account number: ")
            account = customer.accountExists(accountNum)
            if account == None:
              print("Account does not exist")
            else:
              print("\nYour balance is:", account.checkBalance())
                    
          elif choice == "4":
            # View transactions
            if(len(customer.accounts) == 0):
              print("Please create an account before proceeding")
            else:
              accountNum = input("Please enter account number: ")
              account = customer.accountExists(accountNum)
              if account == None:
                print("Account does not exist")
              else:
                account.viewTransactions()

          elif choice == "5":
            # Open Account
            choice = input("Would you like to open a new account? (y or n): ")
            if choice == "y":
              newAccountNum = random.randint(1000,2000)
              customer.openAccount(newAccountNum)
              print("Your new account number is: " + str(newAccountNum))
              customer.viewAccounts()
              
          elif choice == "6":
            # Close account
            accountNum = input("Enter account number: ")
            account = customer.accountExists(accountNum)
            if account == None:
              print("Account does not exist")
            else:
              customer.closeAccount(account)
              print("Account removed successfully")
            
          elif choice == "7":
            # Back
            break
                    
    elif choice == "2":
     
      print("\nWelcome, admin")
      
      while True:
        print("\n1. View Customers")
        print("2. Add Customer")
        print("3. Remove Customer")
        print("4. View ATM Cash")
        print("5. Update ATM Cash")
        print("6. Back")
        choice = input("Enter your choice: ")
                    
        if choice == "1":
          # View customers
          admin.viewCustomers()
                        
        elif choice == "2":
          # Add customer
          name = input("\nEnter customer name: ")
          address = input("Enter customer address: ")
          phone = input("Enter customer phone: ")
          admin.addCustomer(name, address, phone)
          print("Customer added.")
                        
        elif choice == "3":
          # Remove customer
          name = input("\nEnter customer name: ")
          address = input("Enter customer address: ")
          phone = input("Enter customer phone: ")
                        
          for customer in admin.customers:
            if customer.name == name and customer.address == address and customer.phone == phone:
              admin.removeCustomer(customer)
              print("Customer removed.")
              break
            else:
              print("Customer not found.")
                    
        elif choice == "4":
          # View ATM cash
          print("ATM cash:" + str(atm.checkCash()))
                        
        elif choice == "5":
          # Update ATM cash
          amount = float(input("Enter amount to update: "))
          atm.updateCash(amount)
          print("ATM cash updated.")
                        
        elif choice == "6":
          # Back
          break
                
    elif choice == "3":
      # Exit
      break
            
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
