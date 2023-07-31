"""
Make a new class NumbersList that extends the list class.

The NumbersList class should only allow for numeric values (int and float) to be added to the list.

This means you have to overwrite the __init__, append, extend functions.

Add additional methods as described below:

    get_sum() - returns the sum of all the values
    get_average() - returns the average value of all numbers in the list

"""


class NumberList(list):
    def __init__(self, values=None):
        super().__init__(self._filter_numbers(values))

    def _filter_numbers(self, values):
        if values is None:
            return []
        return [value for value in values if isinstance(value, (int, float))]

    def append(self, value):
        if isinstance(value, (int, float)):
            super().append(value)
        else:
            raise ValueError("Only int or float are permitted.")

    def extend(self, values):
        numeric_values = self._filter_numbers(values)
        super().extend(numeric_values)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        if not self:
            return 0
        return sum(self) / len(self)


list_of_numbers = NumberList([1, 2, 3, 4, 5, 6, 7, 8])
print(list_of_numbers)

list_of_numbers.append(22)
print(list_of_numbers)

list_of_numbers.extend([666, 666666])
print(list_of_numbers)

print(list_of_numbers.get_sum())
print(list_of_numbers.get_average())
