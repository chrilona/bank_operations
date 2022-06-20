from __future__ import with_statement
from time import strftime


class Account:
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        self.statement=[]

    def deposit(self,amount):
        self.balance+=amount
        time_of_trans=strftime("%c")
        if amount<=0:
            return f"Deposit must be positive"
        else:
            self.deposits.append(amount)
            return f"You deposited {amount} at {time_of_trans} current balance is {self.balance}"
        
    def withdraw(self,amount):
        transaction_fee=100
        self.amount=amount
        total_withdraw=amount+transaction_fee
        new_balance=self.balance-total_withdraw
        time_of_trans=strftime("%c")
        if amount<=0:
            return f"You cannot withdraw zero less than 0"
        elif total_withdraw<self.balance:
            self.balance-total_withdraw
            return f"You have succesfully withdrawn {amount}Ksh at {time_of_trans}.Your new balance {new_balance}Ksh"
        elif total_withdraw>self.balance:
            return f"Your balance is {self.balance}, you can't withdraw {amount}"
        else:
            self.withdraws.append(amount)
            return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance} and your withdrawals are {self.withdrawals}"

    def deposit_statement(self):
        for amount in self.statement:
            print(f"Your latest deposit is {amount}.Your total deposits are {sum(self.deposit)}")
    
    def withdrawal_statement(self):
        for withdraws in self.statement:
            print(f"Your most recent withdrawal is {withdraws}Ksh.You have withdrawn {len(self.withdraw)} times")

    def full_statements(self):
        timee=strftime("%c")
        for statement in self.statement:
            if statement in self.deposit:
                print(f"{statement[timee]}__deposit__{statement[self.amount]}")
        for statement in self.statement:
            if statement in self.withdraw:
                 print(f"{statement[timee]}__withdraw__{statement[self.amount]}")

    
    def  borrow_loans(self,loan_amount):
        self.loan_amount=loan_amount
        self.interest=0.03*self.loan_amount
        self.total_loan=self.loan_amount+self.interest
        total_deposit=0
        for statement in self.statement:
            total_deposit+=statement["amount"]
        if  loan_amount<=(sum(self.deposits)//3) and (len(self.deposits)>10) and loan_amount>100 and self.balance<=0:
            self.balance+=loan_amount
            print(f"You have been awarded a loan of {loan_amount} your current balance is {self.balance}")
        else:
            print(f"You are not eligible for a loan.Your deposits are {len(self.deposit)} out of 10.Your balance must be 0") 

    def pay_loans(self,amount_payloan):
        self.amount_payloan=amount_payloan
        loan_remaining=self.total_loan-amount_payloan
        new_balance=amount_payloan-self.total_loan
        if amount_payloan>0:
            print(f"You have deposited {amount_payloan} your loan of {self.loan_amount}Ksh.Your new loan balance is {loan_remaining}Ksh")
        elif amount_payloan>loan_remaining:
            print(f"Congratulations!! You have cleared your loan of {self.loan_amount}.Your new balance is{new_balance}")
        else:
            print(f"You have a loan balance of {self.total_loan}")

    def transfer(self,receiver,amount):
        transfer_fee=50
        total_amount=amount+transfer_fee
        if amount<=0:
            return f"You cannot transfer a non-existant amount"
        elif total_amount<=self.balance:
            self.balance-=total_amount
            return f"You have transfered {amount} to {receiver} your current balance is {self.balance}"
        else:
            return f"Failed  transfer {amount}.Your current balance is {self.balance}"
   
               
    
    def current_balance(self):
        return self.balance

acc=Account("lona",8976)

