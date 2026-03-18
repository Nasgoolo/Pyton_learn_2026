value = (input())
if value.isdigit():
    if int(value) % 2 == 0:
        print(f"Entered value {value} is an even number")
    else:
        print(f"Entered value {value} is an odd number")
else:
    print(f"Entered value {value} is a text with length {len(value)}")
