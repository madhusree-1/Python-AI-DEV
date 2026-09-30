from Payment import Payment
class UPI(Payment):
    def processPayment(self):
        print("UPI payment is processing")
    def refundPayment(self):
        print("UPI payment is refunded")
    def validatePayment(self):
        print("UPI payment is validated")