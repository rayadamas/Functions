def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1] == string


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is NOT a palindrome".format(word))

print('-' * 80)
