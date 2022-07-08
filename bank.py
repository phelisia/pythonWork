from datetime import datetime
class Account:
    def __init__(self ,name,account_number,account_type):
        self.name=name
        self.account_number=account_number
        self.account_type=account_type
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=100
        self.loan_balance=0
        

        
        
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
        now=datetime.now()
        if amount<=0:
            return f"deposit amount must be greater than 0 {now}"
        else:
            self.narration={ "date":now, "name":self.name, "amount": amount, "balance" :self.balance}
            self.balance+=amount
            self.deposits.append(amount)
            
            return f" hello {self.name} confirmed you have deposited {amount} and your new balance is {self.balance} on  {now}"
    def withdrawa(self,amount):
        now=datetime.now()
        withdrawal_amount=amount+self.transaction
        if amount >self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return f"amount must be greater than 0"
        else:
            self.narration={ "date":now, "name":self.name, "amount": amount, "balance" :self.balance}
            self.balance-=withdrawal_amount
            self.withdrawals.append(amount)
            return f" hello {self.name} you have withdrawn {amount} your new balance is {self.balance} on {now}"     
    def deposits_statement (self):
        now=datetime.now()
        for depo in self.deposits:
            print(f"You deposited {depo} on {now} ")

    def withdrawal_statements(self):
         now=datetime.now()
         for witho in self.withdrawals:
            print(f" you have withdrawn {witho}")     
    def total_balance(self):
        now=datetime.now()
        return f" your balance is {self.balance} on {now}"
    def full_statement(self):
        now=datetime.now()
        statements=self.deposits+self.withdrawals
        for item in statements:
            statements.sort(key=lambda item: item['date'], reverse=True)
            print(f"{item['date']}_______{item['amount']}")
    def borrow(self,loan):
        total=sum(self.deposits)
        qualification_amount=total*(1/3)
        loan+=loan*(30/100)
        if len(self.deposits) < 10 :
            return f"Sorry {self.name} you must have more than 10 deposits to get a loan"
        elif loan <= 100:
            return f"Sorry {self.name} . Please enter an amount more than 100"
        elif loan >= qualification_amount:
            return f"You cannot borrow more than {total//3}"
        elif self.loan_balance > 0:
            return f"Dear customer, your outstanding loan balance is {self.loan_balance}"
        else:
            self.loan_balance +=loan
            return f"Your loan balance is {self.loan_balance}"
    def loan_repayment(self,amount):
        if amount < self.loan_balance:
            self.loan_balance-=amount
            return f"You have paid {amount} and you have an outstanding balance is {self.loan_balance}"

        else:
            self.loan_balance-=amount
            overpayment=amount-self.loan_balance
            self.balance+=overpayment
            self.loan_balance=0

            return f"You loan is fully paid"   
    def transfer_amount(self,amount,new_account):
        if amount< 0:
            return f"Invalid amount"
        elif amount>=self.balance :
            return f"insufficient balance"   

        elif isinstance(new_account,Account): 
            self.balance-=amount
            new_account.deposit(amount)
            return f"you have transfered{amount}ksh to the with the name of {new_account.name}your new balance is{self.balance}"





      


                
