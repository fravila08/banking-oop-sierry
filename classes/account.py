import csv
from datetime import datetime

class Account:
    accounts=[]
    def __init__(self, id, balance, open_date= datetime.now() ):
        self.id=id
        self.balance= balance
        self.open_date= open_date
        
    def __str__(self):
        return f"ID: {self.id} Balance: {self.balance}"
    
    def __repr__(self):
        return f"DATE: {self.open_date}"
    
    def grab_account(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
    
    def withdraw(self, amount_to_withdraw):
        if int(self.balance) >= amount_to_withdraw:
            self.balance= str(int(self.balance) - amount_to_withdraw)
            return f"withdraw was successful new balance is {self.balance}"
        raise Exception("Not enough funds") 
    
    def deposit(self, amount_to_deposit):
        if amount_to_deposit < 0:
            return "incorrect input"
        self.balance= str(int(self.balance)+amount_to_deposit)
        return f"deposit successfull new balance is {self.balance}"
    
    @classmethod
    def creating_account(self, balance):
        id= str(int(self.accounts[len(self.accounts)-1].id)+1)
        if int(balance) < 0:
            return "incorrect input"
        else:
            self.accounts.append(Account(id, balance))
            return "New account was created"
        
    @classmethod
    def all_accounts(self):
        print("from all accounts")
        for account in self.accounts:
            print(account)
    
    @classmethod
    def opening_csv(self):
        with open('../support/accounts.csv') as csv_accounts:
            account = csv.DictReader(csv_accounts, ['id', 'balance', 'open_date'])
            for row in account:
                self.accounts.append(Account(**row))
        
            

