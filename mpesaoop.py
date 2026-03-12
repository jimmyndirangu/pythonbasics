class MpesaAccount:
    def __init__(self,name,phone,balance):
        self.name=name
        self.phone=phone
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited",amount)
        print(f"Your balance is {self.balance}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"Withdrawn{amount}")
            print(f"New balance is {self.balance}")
        else:
            print("Insufficient funds")
    def check_balance(self):
        print(f"Balance is {self.balance}")

user1=MpesaAccount("Jimmy",254783278934,250)
user1.check_balance()
user1.deposit(1200)
user1.check_balance()
user1.withdraw(500)
user1.check_balance()

user2=MpesaAccount("Alma",254721546149,5000)
user2.deposit(10000)
user2.withdraw(3500)
user2.check_balance()