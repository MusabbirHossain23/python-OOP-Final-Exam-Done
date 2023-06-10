class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            recipient.deposit(amount)
            self.balance -= amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, password):
        user = User(name, email, password)
        self.users.append(user)

    def get_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, password):
        user = User(name, email, password)
        self.bank.users.append(user)

    def get_total_balance(self):
        return self.bank.total_balance

    def get_total_loan_amount(self):
        return self.bank.total_loan_amount

    def enable_loan_feature(self):
        self.bank.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.bank.loan_feature_enabled = False


# Example Usage:

bank = Bank()
admin = Admin(bank)

admin.create_account("Musabbir", "musabbir@example.com", "password1")
admin.create_account("Hossain", "hossain@example.com", "password2")
admin.create_account("Admin", "admin@example.com", "adminpass")

admin.disable_loan_feature()

user1 = bank.get_user("musabbir@example.com")
user2 = bank.get_user("hossain@example.com")

user1.deposit(2000)
user1.withdraw(400)
user1.transfer(user2, 300)
user2.withdraw(500)

print(user1.get_balance())  # Output: 300
print(user2.get_balance())  # Output: 200
print(user1.get_transaction_history())  # Output: ['Deposited: 1000', 'Withdrawn: 500', 'Transferred: 200 to Bob']
print(user2.get_transaction_history())  # Output: ['Deposited: 200', 'Withdrawn: 1000']

print(admin.get_total_balance())  # Output: 0
print(admin.get_total_loan_amount())  # Output: 0
