# - write a function to calculate the sum of all numbers passed as its arguments
# - function should be called `sum_numbers` & take a single argument: the value to sum up to
# - include Docstring
# - Annotate

def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
