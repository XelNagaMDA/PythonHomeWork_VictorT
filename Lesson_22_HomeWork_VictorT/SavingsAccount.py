"""
Create a subclass called SavingsAccount, which extends BankAccount.

    Additional Property:
        interest_rate (private)

    Methods (Overrides):
        __init__(account_number, account_holder_name, interest_rate):
         Constructor to initialize the interest rate for savings accounts.
"""
from Lesson_22_HomeWork_VictorT.BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, interest_rate):
        super().__init__(account_number, account_holder_name)
        self._interest_rate = interest_rate

