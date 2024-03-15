from Bank_account import *
David=BankAccount(5000,"David")
Victoria=BankAccount(1500,"Victoria")




David.GetBalance()
Victoria.GetBalance()


Victoria.Deposit(500)
David.Deposit(5000)


David.withdraw(1000)

David.transfer(15000,Victoria)
David.transfer(9000,Victoria)
Victoria.transfer(7000,David)


Samuel =IntrestRewardAcct(2000,"Samuel")
Samuel.GetBalance()
Samuel.Deposit(200)
Samuel.transfer(200,David)


Robert=SavingsAcct(15000,"Robert")
Robert.GetBalance()
Robert.Deposit(10000)
Robert.transfer(7000,Victoria)



Robert.GetBalance()
Robert.transfer(17000,David)
Robert.GetBalance()