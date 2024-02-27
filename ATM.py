from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class BusinessAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class ATM:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount):
        self.account.withdraw(amount)

    def check_balance(self):
        print(self.account.balance)

def main():
    account = CheckingAccount(123, 0)
    atm = ATM(account)
    
    choice = ""
    while choice != "e":
        choice = input("Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'e' to exit: ")
        if choice == "d":
            amount = int(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == "w":
            amount = int(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "b":
            atm.check_balance()
        elif choice == "e":
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()