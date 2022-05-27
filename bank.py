class Account:
    def __init__(self ,name,account_number,account_type,balance):
        self.name=name
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance
    def withdraw (self):
        withdrawn = float(input("Enter amount to be withdrawn: "))
        if self.balance >= withdrawn:
            self.balance -= withdrawn
            print(f" your account name {self.name} with account number {self.account_number} and account type{self.account_type} and  balance {self.balance} you have withdrawn\n You Withdrew:", withdrawn)
        else:
            print("\n Insufficient balance  ")
    def deposit (self):
        withdrawn = float(input("Enter amount to be withdrawn: "))
        if self.balance >= withdrawn:
            self.balance += withdrawn
            print(f" your account name {self.name} with account number {self.account_number} and account type{self.account_type} and  balance {self.balance} you have withdrawn\n You deposited:", withdrawn)
        else:
            print("\n Insufficient balance  ")        