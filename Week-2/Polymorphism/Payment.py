class Payment:
    def __init__(self,shopping):
        self.shopping= shopping
    def process_payment(self):
        return "The payent has been completely processed"
    
class CreditCardPayment(Payment):
    def process_payment(self):
        return f"The payment has been completely processed using Credit Card for {self.shopping}" 

class PayPalPayment(Payment):
    def process_payment(self):
        return f"The payment has been completely processed using PayPal for {self.shopping}"
    
class BitcoinPayment(Payment):
    def process_payment(self):
        return f"The payment has been completely processed using Bitcoin for {self.shopping}"
    
payment= CreditCardPayment("Birthday")
print(payment.process_payment())
payment1= PayPalPayment("Wedding")
print(payment1.process_payment())
payment2= BitcoinPayment("Trip")
print(payment2.process_payment())
        