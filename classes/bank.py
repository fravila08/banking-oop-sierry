from account import Account
from owners import Owners
import csv

class Bank(Account, Owners):
    matching_table={}
    def __init__(self, name):
        self.name=name
        self.accounts = Account.opening_csv()
        self.owners = Owners.open_csv()
        self.table= self.open_table()
        
    @classmethod
    def open_table(self):
        with open('../support/account_owners.csv') as csv_accounts:
            account = csv.DictReader(csv_accounts, ['account_id', 'owner_id'])
            for row in account:
                self.matching_table[row['account_id']]= row['owner_id']
