class Money:
    def __init__(self,amount:int,balance:int,saving:int,grocery:int,food:int,other:int):
        self._amount = amount
        self._balance = balance
        self._saving = saving
        self._grocery = grocery
        self._food = food
        self._other = other

    def get_amount(self):
        
        return self._amount
    
    def get_balance(self):
        
        return self._balance
    
    def get_saving(self):
        saving = self._amount - self._balance
        return self._saving

    def get_grocery(self):
        grocery = int(input("Enter the amount spent on grocery: "))
        return self._grocery

    def get_food(self):
        food = int(input("Enter the amount spent on food: "))   
        return self.get_food

    def get_other(self):
        other = int(input("Enter the amount spent on others (like petrol): ")) 
        return self._other
