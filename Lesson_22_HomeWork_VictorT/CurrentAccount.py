"""


Create a subclass called CurrentAccount, which also extends BankAccount.

    Additional Property:
        overdraft_limit (private)

    Methods (Overrides):
        __init__(account_number, account_holder_name, overdraft_limit):
        Constructor to initialize the overdraft limit for current accounts.


"""
from Lesson_22_HomeWork_VictorT.BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, overdraft_limit):
        super().__init__(account_number, account_holder_name)
        self._overdraft_limit = overdraft_limit
