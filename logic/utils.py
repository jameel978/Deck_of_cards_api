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
