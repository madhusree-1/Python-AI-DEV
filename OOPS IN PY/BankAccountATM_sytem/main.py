from BankAccount import *
def main():
    print("Bank:",BankAccount.bank_name)
    b1 = BankAccount("Ravi Kumar","Savings",5000.00,"2006")
    print(BankAccount.__str__(b1))
    b2 = BankAccount("Anita Sharma","Current",20000.00,"sree")
    print(BankAccount.__str__(b2))
    print("Total accounts:",BankAccount.total_accounts)
    print(BankAccount.deposit(b1,2000.00))
    print(BankAccount.withdraw(b1,1500,"2006"))
    print(BankAccount.add_annual_interest(b1))
    print(b1.balance)
    print(BankAccount.change_pin(b1,"2006","MadH"))
    
    # incorrect pin
    # print(BankAccount.change_pin(b1,"madh","2006"))

    # insufficent funds
    # print(BankAccount.withdraw(b1,150000,"MadH"))

    # deposit must be not be negative
    # print(BankAccount.deposit(b1,-200.00))

    # attribute error
    # b1.balance = 999999
    # print(b1.balance)
if __name__ == "__main__":
    main()