def lists_to_dict(a, b):
    dict_n = {}
    for i in range(min(len(a), len(b))):
        dict_n[a[i]] = b[i]
    return dict_n


print(lists_to_dict([1, 2, 3], ["one", "two", "three"]))
