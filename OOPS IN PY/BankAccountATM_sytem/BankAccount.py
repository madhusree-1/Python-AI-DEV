class BankAccount:
    bank_name = "State Bank of India"
    total_accounts = 0
    interest_rate = 4.0
    MIN_BALANCE = 500
    _next_account_number = 1001
    def __init__(self,holder_name,account_type,intial_deposit,pin):
        if intial_deposit < BankAccount.MIN_BALANCE:
            raise ValueError(f"Blocked: Initial deposit must be at least Rs.{BankAccount.MIN_BALANCE}")
        self.holder_name = holder_name
        self._account_type = account_type
        self._balance = intial_deposit
        self.__pin = pin
        BankAccount.total_accounts += 1
    @property
    def account_number(self):
        if self.total_accounts == 1:
            return self._next_account_number
        else:
            self._next_account_number += 1
            return self._next_account_number
    @property
    def balance(self):
        return (f"Balance now: {self._balance}")
    def deposit(self,amount):
        # to check if deposit is positive
        if not BankAccount.is_valid_amount(amount):
            raise ValueError("Blocked (negative): Deposit amount must be positive")
        
        self._balance += amount
        return (f"Deposited Rs.{amount} -->  Rs.{self._balance}")
    def withdraw(self,amount,pin):
        if pin != self.__pin:
            raise ValueError("Blocked (wrong PIN): Incorrect PIN")
        if not BankAccount.is_valid_amount(amount):
            raise ValueError("Blocked (negative): Withdrawal amount must be positive")
        if (self._balance - amount) < BankAccount.MIN_BALANCE:
            raise ValueError(f"Blocked (Below min): Minimum balance of Rs.{BankAccount.MIN_BALANCE} must remain")
        
        self._balance -= amount
        return (f"Withdrew Rs.{amount} --> Rs.{self._balance}")
    def _verify_pin(self,pin):
        return len(str(pin))==4
    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            raise ValueError("Blocked (wrong PIN): Incorrect PIN")
        if not BankAccount._verify_pin(self,old_pin):
            raise ValueError("Blocked: New PIN must be exactly 4 digits")
        self.__pin = new_pin
        return ("PIN changed successfully")
    def add_annual_interest(self):
        interest = (self._balance * BankAccount.interest_rate) / 100
        self._balance += interest
        return (f"Interest added: {interest}")
    @classmethod
    def get_total_accounts(cls):
        return BankAccount.total_accounts
    @staticmethod
    def is_valid_amount(amount):
        if(amount >0):
            return True
        else:
            return False
    def __str__(self):
        return (f"Account[{self.account_number}] {self.holder_name} | {self._account_type}| Rs.{self._balance}")
