class BankAccount():
    def  __init__(self,bal=0):
        self.__bal=bal
        pass
    def deposit(self,amount):
        self.__bal+=amount
        print("Deposited Successfuly")
    def withdraw(self,amount):
        if self.__bal>=amount:
            self.__bal-=amount
            print("withdrawed sucessfully")
        else:
            print("Insufficient Balance")
    def get_bal(self):
        print(f"Balance->{self.__bal}")
b=BankAccount()
b.deposit(3000)
b.withdraw(1)
b.get_bal()