def deduped_using_set(items):
    """Return new list from items with duplicates removed."""

    if items ==[]:
        return []

    unique_items_set = set(items) #sets dont maintain order though
    unique_items_list = list(unique_items_set)

    return unique_items_list

def deduped(items):
    """Return new list from items with duplicates removed."""

    if items == []:
        return []

    unique_items_set = set() #use a set to search within - faster runtime
    unique_items_list = []

    for item in items:
        if item not in unique_items_set:
            unique_items_list.append(item)
            unique_items_set.add(item)

    return unique_items_list

print(deduped([1, 2, 1, 1, 3]))

