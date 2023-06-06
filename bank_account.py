#creating a class
class BankAccount:
    
    #construction method
    def __init__(self, account_number, account_holder, balance = 0) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited {amount}$. Your current balance is {self.balance}')
    
    def withdraw(self, amount):
        #self.balance -= amount
        #print(f'You withdrew {amount}$. Your current balance is {self.balance}')
        self.balance >= amount
        print(f'You have not an enough money. Your current balance is {self.balance}')

    def check_balance(self):
        print(f'Account Holder: {self.account_holder}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: {self.balance}')

account_1 = BankAccount('123654', 'Jane Dou', 100)
account_2 = BankAccount('789456', 'James Kim')

account_1.deposit(1000)
account_2.deposit(30)
account_1.withdraw(20)
account_2.withdraw(31)
account_1.check_balance()
account_2.check_balance()

