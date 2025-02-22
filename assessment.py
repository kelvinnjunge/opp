#Importing necessary libraries
import uuid
from datetime import datetime 

# Creating Expense class

class Expense :
    def __init__(self,title,amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at  = self.created_at

   # update function that allows updating the title and amount and updating the updated timestamp

    def update(self,title=None,amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

   # Dictionary that represents the expense

    def to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "amount":self.amount,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
    

# creating expense database 

class ExpenseDatabase:
    # creating in it function 
    def __init__(self):
        self.expenses = []
    

    #Adding all the expenses 
    def add_expense(self,expense):
        self.expenses.append(expense)
    

    #Removing all the expenses 
    def remove_expense(self,expense_id):
        self.expenses = [x for x in self.expenses if x.id != expense_id]
    

    #Returning all the expenses by id 
    def get_expense_by_id(self ,expense_id):
        for x in self.expenses:
            if x.id == expense_id:
                return x
        return None 
    
    #Returning all the expenses by title 
    def get_expense_by_title(self,title):
        return_expenses = []
        for x in self.expenses:
            if x.title.lower() == title.lower():
                return_expenses.append(x)
        return return_expenses
    
    #Returing all the expenses in dictionary form 
    def to_dict(self):
        return [x.to_dict() for x in self.expenses]
    

if __name__ == "__main__":
    db = ExpenseDatabase()

    expense1 = Expense("Car",1000)
    expense2 = Expense("Furniture",10000)

    #adding all the expense
    db.add_expense(expense1)
    db.add_expense(expense2)

    #printing all the expenses 
    print(db.to_dict())

    

