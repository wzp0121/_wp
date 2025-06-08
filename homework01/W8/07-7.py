def dict_to_string(d):
    return ', '.join(f"{key}:{value}" for key, value in d.items())
    
print(dict_to_string({'a': 1, 'b': 2})) 