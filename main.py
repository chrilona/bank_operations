from __future__ import with_statement
from datetime import datetime
from operator import ne
from time import strftime


class Account:
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        self.statement=[]
        self.counts=len(self.deposits)
        self.time_of_trans=datetime.now()
        self.time_of_trans=strftime("%c")

    def deposit(self,amount):
        self.balance+=amount
        if amount<=0:
            return f"Deposit must be positive"
        else:
            narration={"You have deposited":amount,"at":self.time_of_trans,"Your current balance is":self.balance}
            self.deposits.append(narration)
            return f"Congratulations,{self.account_name}!!.You deposited {amount} at {self.time_of_trans} current balance is {self.balance}"
    def withdraw(self,amount):
        transaction_fee=100
        self.amount=amount
        total_withdraw=amount+transaction_fee
        new_balance=self.balance-total_withdraw
        narration={"You withdrew":amount,"at":self.time_of_trans,"Your current balance is":self.balance}
     
        if amount<=0:
            return f"You cannot withdraw zero less than 0"
        elif total_withdraw<self.balance:
            self.balance-=total_withdraw
            self.withdraws.append(narration)
            return f"You have succesfully withdrawn {amount}Ksh at {self.time_of_trans}.Your new balance {self.balance}Ksh"
        elif total_withdraw>self.balance:
            return f"Your balance is {self.balance}, you can't withdraw {amount}"
        else:
            self.withdraws.append(narration)
            return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance} and your withdrawals are {self.withdrawals}"

    def deposit_statement(self):
          print( self.deposits,end="\n")
    def withdrawal_statement(self):
           print( self.withdraws,end="\n")  
    def full_statements(self):
        statement=self.withdraws+self.deposits
        for state in statement:
            print(state)
    def  borrow_loans(self,loan_amount):
        self.loan_amount=loan_amount
        self.interest=0.03*self.loan_amount
        self.total_loan=self.loan_amount+self.interest
        total_deposit=0
        deposits_number=len(self.deposits)
        for statement in self.statement:
            total_deposit+=statement["amount"]
        if  loan_amount<=(sum(self.deposits)//3) and deposits_number>10 and loan_amount>100 and self.balance<=0:
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
            new_balance=self.balance-total_amount
            return f"You have transfered {amount} to {receiver} your current balance is {new_balance}"
        else:
            return f"Failed  transfer {amount}.Your current balance is {self.balance}"
   
    def current_balance(self):
        return f"{self.balance} is your current balance"

acc=Account("lona",8976)

