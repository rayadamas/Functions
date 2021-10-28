numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")

# star represents that this parameter will be replaced by an unpacked tuple
# the star causes Python to follow a few simple rules & packs the values up into a tuple
# *args also acts as an `X` value for our function
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
