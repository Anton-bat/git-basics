class Account:
    def __init__(self, balance, account_holder=0) -> None:
        self.__balance = balance
        self._account_holder = account_holder
    
    def ret(self):
        return self.__balance

a = Account(10)

print(a.ret())        


