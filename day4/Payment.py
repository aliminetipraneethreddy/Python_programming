class Payment():
    def __init__(self,amount):
        self.amount=amount
        pass
    def pay(self):
        pass

class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        self.amount=amount
    def pay(self):
        print(f"Cash Payment {self.amount}")
class CardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        self.amount=amount
    def pay(self):
        print(f"Card Payment{self.amount}")
class UPIPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        self.amount=amount
    def pay(self):
        print(f"UPI Payment{self.amount}")
p=[CashPayment(500),CardPayment(5000),UPIPayment(50000)]
for i in p:
    i.pay()
