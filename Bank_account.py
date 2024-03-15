class BalanceException(Exception):
    pass
    




class BankAccount:
    def __init__(self,initialAmount,acctname) :
        self.balance=initialAmount
        self.name=acctname
        print(f"\nAccount'{self.name}'created.\nBalance=${self.balance:.2f}")
    
    def GetBalance(self):
        print(f"\nAccount'{self.name}'balance=${self.balance:.2f}") 
        
        
        
        
    def Deposit(self,amount):
        self.balance=self.balance + amount
        print("\nDeposit complete.....✅✅✅✅") 
        self.GetBalance()
        
        
        
        
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,account'{self.name}'only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self,amount):
        try:
           self.viableTransaction(amount)
           self.balance= self.balance - amount
           print("\nWithdraw complete...✅✅✅✅")
           self.GetBalance()
        except BalanceException as error:
            print("\nWithdraw interruptted.....❌❌❌❌:{error}")
            
            
            
    def transfer(self,amount,account):
        try:
            print(f'\n***********\n\nBeginning transfer.....📌📌')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.Deposit(amount)
            print(f"\nTransfer completed!✅✅✅✅\n\n*********")
        except BalanceException as error:
            print(f"\nTransfer interruptted.... ❌❌❌❌{error}")
           
          
     
class IntrestRewardAcct(BankAccount):
    def Deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete!......✅✅✅✅")
        self.GetBalance()




class SavingsAcct(IntrestRewardAcct):
    def __init__(self, initialAmount, acctname):
        super().__init__(initialAmount, acctname)
        self.fee =5 
        
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance - (amount+self.fee)
            print("\nWithdraw complete!.....✅✅✅✅")
        except BalanceException as error:
            print(f"\nWithdraw interuppted.... ❌❌❌❌:{error}")
      
    