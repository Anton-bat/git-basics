from abc import ABC, abstractmethod
import random

class Customer(ABC):
    def __init__(self, name, email, customer_id) -> None:
        self.name = name
        self.email = email
        self.customer_id = customer_id

    def get_info(self):
        return f"{self.name}, {self.email}, {self.customer_id}"
    
class BankAccount(ABC):
    def __init__(self, owner, initial_balance=0) -> None:
        self.balance = initial_balance
        self.owner = owner
        self.account_number = self.generate_acc_number()
    
    def generate_acc_number(self):
        return "".join(str(random.randint(1,9)) for _ in range(10))

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def get_account_info(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, owner, initial_balance=0) -> None:
        super().__init__(owner, initial_balance)
    
    def deposit(self, amount):
        if amount <= 0:
            print('no money')
        self.balance += amount
        print(f'added, new balance {self.balance}')

    def withdraw(self, amount):
        if amount <= 0:
            print('no money')
        self.balance -= amount
        print(f'withdrawed, new balance {self.balance}')
    
    def get_account_info(self):
        return f'Owner: {self.owner.get_info()}, Balance: {self.balance}, Account Number: {self.account_number}'

customer_1 = Customer("Toha", "dd@bal.ua", 1455222)
account_1 = SavingsAccount(customer_1, 500)

print(customer_1.get_info())
print(account_1.get_account_info())

account_1.deposit(800)

print(customer_1.get_info())
print(account_1.get_account_info())

account_1.withdraw(600)

print(customer_1.get_info())
print(account_1.get_account_info())