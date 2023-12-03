def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    cp = [ix for ix in my_list]
    cp[idx] = element
    return cp
