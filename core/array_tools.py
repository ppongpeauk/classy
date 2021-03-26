def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}
def on_first_index(d):
    return {x:y[0] if isinstance(y, list) else y for x, y in d.items()}