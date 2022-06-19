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
        self.newdict={}
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
            self.narration=f" hello {self.name} you have deposited {amount} and your new balance is  {self.balance}  {now}"
            self.balance+=amount
            self.deposits.append(amount)
            self.newdict["date"]=now
            self.newdict["amount"]=amount
            self.newdict["narration"]=self.narration
            return f" hello {self.name} confirmed you have deposited {amount} and your new balance is {self.balance} on  {now}"
    def withdrawa(self,amount):
        now=datetime.now()
        withdrawal_amount=amount+self.transaction
        if amount >self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return f"amount must be greater than 0"
        else:
            self.narration=f" hello  {self.name}  confirmed you have withdrawn {amount} your new balance is{self.balance} on{ now}" 
            self.balance-=withdrawal_amount
            self.withdrawals.append(amount)
            self.newdict["date"]=now
            self.newdict["amount"]=amount
            self.newdict["narrations"]=self.narration

            
            return f" hello {self.name} you have withdrawn {amount} your new balance is {self.balance} on {now}"     
    def deposits_statement (self):
        now=datetime.now()
        for depo in self.deposits:
            print(f"You deposited {depo}  {now}")

    def withdrawal_statements(self):
         now=datetime.now()
         for witho in self.withdrawals:
            print(f" you have withdrawn {witho}  on {now}")     
    def total_balance(self):
        now=datetime.now()
        return f" your balance is {self.balance} on {now}"
    def full_statement(self):
        now=datetime.now()
        full=[self.deposits+self.withdrawals]
        for x in full:
            print(f"{now}{x}")
    def borrow(self,loan):
        sum=0
        for depo in self.deposits:
            sum+=depo
            print(sum)
        if len(self.deposits)<10:
            return f" you have more than 10 depoist and your loan is{loan}"
        elif loan>100:
            return f"you qualify for a loan"
        elif :
            pass
        elif self.loan_balance==0:
            pass

            
        else:
            print("not qualified for a loan")    

      


                
