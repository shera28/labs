class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print('balance:', self.balance)
        else:
            print("No money")


a = Account('Ada', 1000)
a.deposit(2000)
a.withdraw(3001)
a.withdraw(2999)