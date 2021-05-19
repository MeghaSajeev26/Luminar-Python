#account creation,deposit,withdraw

class Bank():
    Bank_name="Axis Bank"
    def account(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        self.minbalance=5000
        self.balance=self.minbalance
        print("Bank name:",Bank.Bank_name)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Place:",self.place)
    def deposit(self,deposit):
        self.deposit=deposit
        self.balance+=self.deposit
        print("Your account has been credited with:",self.deposit)
        print("Current Balance:",self.balance)
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        if self.balance < self.withdraw:
            print("Insufficient balance")
        else:
            print("Account debited with:",self.withdraw)
            self.balance-=self.withdraw
        print("Available Balance:",self.balance)
obj=Bank()
obj.account("Amal",25,"Palakkad")
obj.deposit(10000)
obj.withdraw(5000)
