from Payment import Payment
class Cash(Payment):
    def processPayment(self):
        print("cash payment is processing")
    def refundPayment(self):
        print("cash payment is refunded")
    def validatePayment(self):
        print("Cash payment is validated")