import csv

class Owners:
    all_owners=[]
    def __init__(self, id, last, first, address, city, state):
        self.id= id
        self.last=last
        self.first= first
        self.address= address
        self.city = city
        self.state = state
        
    def __str__(self):
        return f"{self.first} has an id of {self.id}"
    
    @classmethod
    def all_custormer(self):
        for customer in self.all_owners:
            print(customer)
    
    @classmethod
    def open_csv(self):
        with open('../support/owners.csv') as csv_customers:
            customer = csv.DictReader(csv_customers, ['id', 'last', 'first', 'address', 'city', 'state'])
            for row in customer:
                self.all_owners.append(Owners(**row))
            print(self.all_owners)
