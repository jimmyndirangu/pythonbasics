from abc import ABC,abstractmethod
#_____ENCAPSULATION______
class MpesaAccount:
    def __init__(self,name,balance):
        self.name=name
        self._balance=balance #private variable

    def deposit(self,amount):
           self._balance+=amount
           print(f"{amount} deposited. Balance:{self._balance}")
    def withdraw(self,amount):
         if amount <=self._balance:
            self._balance-=amount
            print(f"{amount} withdrawn. Balance:{self._balance}")
            return True
         return False
    
    def get_balance(self):
         return self._balance
    


# __________ABSTACTION_________
class MpesaService(ABC):
     
     @abstractmethod
     def access_service(self,account,amount):
          pass


#_________SEND MONEY________
class SendMoney(MpesaService):
     def access_service(self, account, amount):
        if account.withdraw(amount):
           print(f"Sent {amount} to another user.")
        else:
            print("Transaction failed: insufficient balance.")


#________LIPA NA MPESA_______
class LipaNaMpesa(MpesaService):
    def access_service(self, account, amount):
        if account.withdraw(amount):
            print(f"Paid {amount} to merchant using Lipa na M-Pesa.")
        else:
            print("Payment failed:Insufficient funds")


#________FULIZA_______
class Fuliza(MpesaService):
    def __init__(self,limit):
        self.limit=limit
        
    def access_service(self, account, amount):
        balance=account.get_balance()
        if amount<=balance:
            account.withdraw(amount)
            print("Transaction completed without Fuliza.")
        elif amount<=balance+self.limit:
            overdraft=amount-balance
            account.withdraw(balance)
            print(f"Transaction completeed using fuliza ovedraft:{overdraft}")
        else:
            print("Transaction exceeds fuliza limit.")


#__________M-SHWARI SAVINGS________
class Mshwari(MpesaService):
    def __init__(self):
        self.savings=0
    def access_service(self, account, amount):
        if account.withdraw(amount):
            self.savings+=amount
            print(f"{amount} saves to M-Shwari. Total savings:{self.savings}")
        else:
            print("Not enough balance to save.")


#__________LOANS________
class Loan(MpesaService):
    def __init__(self,limit):
        self.limit=limit
        self.loan_balance=0
    def access_service(self, account, amount):
        if amount<=self.limit:
            account.deposit(amount)
            self.loan_balance+=amount
            print(f"Loan approved:{amount}. Total loan owed:{self.loan_balance}")
        else:
            print("Loan request exceeds limit.")

    
#_______MAIN PROGRAM_______
account=MpesaAccount("Brian",500)

send_money=SendMoney()
lipa=LipaNaMpesa()
fuliza=Fuliza(300)
mshwari=Mshwari()
loan=Loan(1000)

print("Initial balance:",account.get_balance())

#save to Mshwari
mshwari.access_service(account,200)

#Send money
send_money.access_service(account,100)

#Pay merchant
lipa.access_service(account,150)

#Use Fuliza
fuliza.access_service(account,400)

#Take loan
loan.access_service(account,500)

print("Final Balance:",account.get_balance())
