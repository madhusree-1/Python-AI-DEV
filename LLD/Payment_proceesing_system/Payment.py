#using the brute force
# from abc import abstractmethod,ABC
class Payment:
    # multiple if - else blocks violating the srp
    # when adding the paypal and wallet payment it is modifying so violating the OCP 
    def __init__(self,name,age,payment_type):
        self.name = name
        self.age = age
        self.payment_type = payment_type
    # def processPayment(self,payment_type):
    #     if(self.payment_type == "CreditCard"):
    #         pass
    #     elif(self.payment_type == "UPI"):
    #         pass
    #     elif(self.payment_type == "Cash"):
    #         pass

    # def refundPayment(self,payment_type):
    #     if(self.payment_type == "CreditCard"):
    #         pass
    #     elif(self.payment_type == "UPI"):
    #         pass
    #     elif(self.payment_type == "Cash"):
    #         pass

    # def validatePayment(self,payment_type):
    #     if(self.payment_type == "CreditCard"):
    #         pass
    #     elif(self.payment_type == "UPI"):
    #         pass
    #     elif(self.payment_type == "Cash"):
    #         pass
    # @abstractmethod
    def processPayment(self):
        return 
    # @abstractmethod
    def refundPayment(self):
        pass
    # @abstractmethod
    def validatePayment(self):
        pass


       
            
