import unittest
from Infra.Api_wrapper import APIWrapper
from Logic.Deck_of_cards import DeckOfCards
from Logic.Utils import *


class DeckOfCards_piles_tests(unittest.TestCase):

    def setUp(self) -> None:
        my_api = APIWrapper()
        self.api_logic = DeckOfCards(my_api)
        self.card_deck = self.api_logic.A_brand_new_deck()
        self.deck_id = self.card_deck['deck_id']

    def test_creating_card_piles(self):
        card_deck = self.api_logic.draw_a_card(self.deck_id, count=5)
        piles_card_deck = self.api_logic.add_to_piles(self.deck_id,"Jameel",get_cards_names_from_json(card_deck))
        remaining_cards = piles_card_deck['remaining']
        piles_in_deck = piles_card_deck['piles']
        self.assertTrue(card_deck['success'])
        self.assertEqual(remaining_cards,47)
        self.assertEqual(piles_in_deck,{'Jameel': {'remaining': 5}})

    def test_creating_multi_card_piles(self):
        card_deck = self.api_logic.draw_a_card(self.deck_id, count=5)
        pulled_cards_first_hand = get_cards_names_from_json(card_deck)
        self.api_logic.add_to_piles(self.deck_id,"Jameel_pile_1",pulled_cards_first_hand)
        card_deck = self.api_logic.draw_a_card(self.deck_id, count=4)
        pulled_cards_second_hand = get_cards_names_from_json(card_deck)
        piles_card_deck = self.api_logic.add_to_piles(self.deck_id, "Jameel_pile_2", pulled_cards_second_hand)
        self.assertEqual(piles_card_deck['remaining'],43)
        self.assertIn('Jameel_pile_1',piles_card_deck['piles'].keys())
        self.assertIn('Jameel_pile_2',piles_card_deck['piles'].keys())
        self.assertEqual(5,piles_card_deck['piles']['Jameel_pile_1']['remaining'])
        self.assertEqual(4,piles_card_deck['piles']['Jameel_pile_2']['remaining'])

    def test_creating_pull_from_card_piles(self):
        card_deck = self.api_logic.draw_a_card(self.deck_id, count=5)
        card_names = get_cards_names_from_json(card_deck)
        self.api_logic.add_to_piles(self.deck_id,"Jameel_pile_1",card_names)
        empty_card_piles = self.api_logic.draw_from_pile(self.deck_id, "Jameel_pile_1", card_names)
        pulled_cards = get_cards_names_from_json(empty_card_piles)
        self.assertEqual(pulled_cards,card_names)



