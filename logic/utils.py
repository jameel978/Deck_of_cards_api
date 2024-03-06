import json
import inspect
import types
def are_all_cards_in_deck_unique(cards):
    # Convert the list to a set to remove duplicate items
    lst = []
    for card in cards:
        lst.append(card['code'])
    unique_set = set(lst)

    # If the length of the set is equal to the length of the original list, all items are unique
    if len(unique_set) == len(lst):
        return True
    else:
        return False
def get_cards_names_from_json(card_drawn):
    return ",".join(card["code"] for card in card_drawn['cards'])


def get_all_tests(my_class):
    methodList = [v for n, v in inspect.getmembers(my_class, inspect.ismethod) if isinstance(v, types.MethodType)]
    test_list = [test.__name__ for test in methodList if "test_" in test.__name__]
    return test_list

def prepair_all_tests(test_classes):
    lst = []
    for test_class in test_classes:
        for i in get_all_tests(test_class()):
            lst.append((test_class,i))
    return lst



def read_json(location):
    with open(location) as f:
        data = json.load(f)
    return data