from Payment import Payment
class PayPal(Payment):
    def processPayment(self):
        print("PayPal payment is processing")
    def refundPayment(self):
        print("PayPal payment is refunded")
    def validatePayment(self):
        print("Paypal payment is validated")