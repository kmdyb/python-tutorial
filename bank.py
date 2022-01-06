from result import Ok, Error


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return Ok("Wypłacono pieniądze", amount)
        return Error("Nie wypłacono pieniędzy", amount)

    def __str__(self):
        return str(self.balance)


class MinimalBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimalbalance=1000):
        super().__init__(balance)   # odwołanie to klasy-rodzica
        self.minimalbalance = minimalbalance

    def try_withdraw(self, amount):
        if self.balance - amount > self.minimalbalance:
            return super().try_withdraw(amount)
        else:
            return Error("Błąd, próba przekroczenia progu", amount)
