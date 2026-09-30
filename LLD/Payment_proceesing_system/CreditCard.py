from Payment import Payment
class CreditCard(Payment):
    def processPayment(self):
        print("credit card payment is processing")
    def refundPayment(self):
        print("credit card payment is refunded")
    def validatePayment(self):
        print("credit card payment is validated")
        
