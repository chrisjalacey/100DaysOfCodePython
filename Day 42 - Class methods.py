"""
Day 42 - Class methods
Create a class for a bank account with methods for deposit and withdraw
"""

class Bank:
    def __init__(self, accountNo) -> None:
        self.accountNo = accountNo
        self.balance = 0
        #self.amount = amount
        
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print (f"Depositing £{amount} to account {self.accountNo}. Your balance is now £{self.balance}")

    def withdrawal(self, amount):
        self.amount = amount
        self.balance -= self.amount
        print (f"Withdrawing £{amount} from account {self.accountNo}. Your balance is now £{self.balance}")

    def updateAccountNo(self,newAccountNo):
        self.accountNo = newAccountNo

    def printBalance(self):
        print(f"Account {self.accountNo} balance: £{self.balance}")

user1 = Bank(1)
user1.deposit(1)
user1.deposit(50)
user1.withdrawal(35)

user1.updateAccountNo(3)
user1.printBalance()

user1.withdrawal(10)

user2 = Bank(2)
user2.deposit(5)
user1.printBalance()