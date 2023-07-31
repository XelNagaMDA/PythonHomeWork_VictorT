"""


Create a class called BankAccount.

    Properties:
        account_number (private)
        account_holder_name (private)
        balance (private)

    Methods:
        __init__(account_number, account_holder_name): Constructor to initialize account number,
        account holder name, and set balance to 0.
        get_account_number(): Get the account number.
        get_account_holder_name(): Get the account holder name.
        get_balance(): Get the account balance.
        deposit(amount): Deposit money into the account.
        withdraw(amount): Withdraw money from the account.


"""

class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = 0

    def get_account_number(self):
        return self._account_number

    def get_account_holder_name(self):
        return self._account_holder_name

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount


