def add(num1:int, num2:int):
    return num1 + num2
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds in account")
            #raise ZeroDivisionError()
        self.balance -= amount  

    def collect_interest(self):
        self.balance *= 1.1