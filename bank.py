class Account:
    def __init__(self ,name,account_number,account_type):
        self.name=name
        self.account_number=account_number
        self.account_type=account_type
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]

        
        
    # def withdraw (self):
    #     withdrawn = float(input("Enter amount to be withdrawn: "))
    #     if self.balance >= withdrawn:
    #         self.balance -= withdrawn
    #         print(f" your account name {self.name} with account number {self.account_number} and account type{self.account_type} and  balance {self.balance} you have withdrawn\n You Withdrew:", withdrawn)
    #     else:
    #         print("\n Insufficient balance  ")
    # def deposit (self):
    #     withdrawn = float(input("Enter amount to be deposited: "))
    #     if self.balance >= withdrawn:
    #         self.balance += withdrawn
    #         print(f" your account name {self.name} with account number {self.account_number} and account type{self.account_type} and  balance {self.balance} you have withdrawn\n You deposited:", withdrawn)
    #     else:
    #         print("\n Insufficient balance  ")    
    # 
    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount must be greter than o"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"'{self.balance}"
    def withdrawa(self,amount):
        transaction_fee=100
        withdrawal_amount=amount+transaction_fee
        if amount >self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return f"amount must be greater than 0"
        else:
        
            self.balance-=withdrawal_amount
            self.withdrawals.append(amount)
            
            return f" hello {self.name}you have withdrawn{amount} your new balance is{self.balance}"     
    def deposits_statement (self):
        for depo in self.deposits:
            print(f"You deposited{depo}")

    def withdrawal_statements(self):
        for witho in self.withdrawals:
            print(f" you have withdrawn{witho}")     
    def total_balance(self):
        return self.balance

                
