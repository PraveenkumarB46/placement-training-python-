def frequency_dict(lst):
    return {item: lst.count(item) for item in set(lst)}

print(frequency_dict([1, 2, 2, 3]))  
