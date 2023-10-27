class Account:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def print_balance(self):
        print(f"Balance For Account {self.acc_no} is Ksh {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc1 = Account("June", "001", 75000)
acc2 = Account("Alice", "002", 23490)

acc1.deposit(5000)
acc1.print_balance()
acc1.withdraw(12000)
acc1.print_balance()

# xampp
country = "Kenya"
a = 10

