class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._history = []
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._history.append(['deposit', amount])
            return self._balance
        elif amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        if self._balance < amount:
            raise ValueError("Недостаточно средств")
        else:
            self._balance -= amount
            self._history.append(['withdraw', amount])
            return self._balance
    
    def get_history(self):
        return self._history.copy()
        

account = BankAccount("Jack", 1000)

print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(200)
print(account.balance)
account.withdraw(1200)
print(account.balance)

print(account.get_history())
