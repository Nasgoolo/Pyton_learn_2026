def check_even():
    return lambda num: "Even" if num % 2 == 0 else "Odd"


is_even = check_even()
print(is_even(5))
