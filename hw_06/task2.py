def check_age(age):
    if not isinstance(age, int) or 0 < int(age) <= 110:
        return "Error"

    if int(age) >= 18:
        return "Adult"
    else:
        return "Child"


print(check_age(20))
