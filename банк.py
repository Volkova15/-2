class BankAccount:
    def init(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На рахунок {self.account_number} додано {amount}. Новий баланс: {self.balance}")
        else:
            print("Сума для депозиту має бути більше нуля.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів на рахунку")
        elif amount > 0:
            self.balance -= amount
            print(f"З рахунку {self.account_number} знято {amount}. Новий баланс: {self.balance}")
        else:
            print("Сума для зняття має бути більше нуля.")

if __name__ == "main":
    account = BankAccount("123456789", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)