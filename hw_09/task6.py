def unique(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


print(unique([1, 2, 3, 3, 4, 4]))
