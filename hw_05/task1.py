text = input()

for i in text:
    if i.isdigit():
        if int(i) % 2 == 0:
            print(f"The symbol {i} is an even digit")
        else:
            print(f"The symbol {i} is an odd digit")
    elif i.isalpha():
        if i.isupper():
            print(f"The symbol {i} is an uppercase letter")
        else:
            print(f"The symbol {i} is a lowercase letter")
    else:
        print(f"The symbol {i} is neither a digit nor a letter")
