class Account:
    def __init__(self, balance, account_holder=0) -> None:
        self._balance = balance
        self._account_holder = account_holder
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("zero balance")

a = Account(10)

print("balance", a.balance)       

a.balance = -5

print(a.balance)

