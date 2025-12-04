class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough funds.")

    def display_balance(self):
        print(f"Hello, {self.name} your current balance is: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def new_account(self, account):
        self.accounts.append(account)

    def find_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
            else:
                return "Account not found."

    def all_accounts(self):
        for account in self.accounts:
            account.display_balance()


hugo = BankAccount("Hugo", 90)

hugo.deposit(10)

bank = Bank()
bank.new_account(hugo)
bank.all_accounts()
