def add_to_list_index(lst, value, index=None):
    if index is not None:
        lst.insert(index, value)
    else:
        lst.append(value)
