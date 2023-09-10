# Unlimited arguments

# Unlimited Positional arguments * creates tuple
def print_alot(*args):
    for n in args:
        print(n)


# print_alot("hello", "hi", 1, 5, 3)


def dont_have_to_use_args(*hello):
    result = ""
    for item in hello:
        result += f"{item} "
    print(result)

# dont_have_to_use_args("hello", "hi", 1, 5, 3, "see no args")


def my_add(*args):
    result = 0
    for num in args:
        result += num
    return result

# print(my_add(1,5,8,10,3,4,4,2.3))


def shout_or_not(*args):
    result = ""
    for item in args:
        result += f"{item} "
    if args[-1] == "!":
        print(result.upper())
    else:
        print(result)

# shout_or_not("hello", "how", "loud", "!")

# shout_or_not("hello", "how", "loud", ".")

# creating unlimited keyword or named argument functions ** creates dictionary


def this_is_a_kwarg(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(f"A name is {kwargs['name']}")


# this_is_a_kwarg(one=1, two=2, four=4, name="beth")

class Car:

    def __init__(self, color, **kw):
        self.make = kw.get("make")
        # using .get will return "None" if it doesn't exist instead of error
        self.year = kw.get("year")
        self.color = color


new_car = Car("blue", make="Ford",)
print(new_car.color)
print(new_car.make)
print(new_car.year)


