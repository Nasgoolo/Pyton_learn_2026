def mirror():
    return lambda num: -num


m = mirror()

print(m(10))
