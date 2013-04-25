def sort_key(dict):
    return sorted(dict)  # return a list of values sorted by key


def sort_value(dict):
    return sorted(dict, key=dict.get, reverse=True)  # return a list keys sorted by value
