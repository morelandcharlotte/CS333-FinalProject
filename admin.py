# Name: Charlotte Moreland
# Date: 4/24/23
# Assignment: CS 333 Final Project
# Filename: admin.py

from customer import Customer

class Admin:
  
  def __init__(self):
    self.customers = []

  def addCustomer(self, name, address, phone):
    customer = Customer(name, address, phone)
    self.customers.append(customer)
    return customer

  def removeCustomer(self, customer):
    self.customers.remove(customer)

  def viewCustomers(self):
    for customer in self.customers:
      print(" - " + str(self.customers.index(customer) + 1) + " - ")
      print("Customer Name: " + customer.name)
      print("Customer Address: " + customer.address)
      print("Customer Phone: " + customer.phone)

  def getCustomerByName(self, name):
    for customer in self.customers:
      if name == customer.name:
        return customer
        break
    return None
    
    
    
