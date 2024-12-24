def flatten_dict(d, parent_key='', sep='.'):
    """
    Flattens a nested dictionary.

    :param d: Dictionary to flatten
    :param parent_key: Key prefix for nested dictionaries (used internally during recursion)
    :param sep: Separator between keys in the flattened dictionary
    :return: A flattened dictionary
    """
    flat_dict = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):  # If the value is a dictionary, recurse
            flat_dict.update(flatten_dict(v, new_key, sep))
        else:  # If the value is not a dictionary, add it directly
            flat_dict[new_key] = v
    return flat_dict

# Example usage
nested_dict = {"a": {"b": {"c": 1}}, "d": 2}
flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
