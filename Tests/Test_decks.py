import unittest
from Infra.Api_wrapper import APIWrapper
from Logic.Deck_of_cards import DeckOfCards
from Logic.Utils import *


class DeckOfCards_decks_tests(unittest.TestCase):

    def setUp(self) -> None:
        my_api = APIWrapper()
        self.api_logic = DeckOfCards(my_api)

    def test_get_brand_new_deck(self):
        card_deck = self.api_logic.A_brand_new_deck()
        self.assertTrue(card_deck['success'])
        self.assertFalse(card_deck['shuffled'])
        self.assertEqual(card_deck['remaining'],52)

    def test_get_band_new_deck_with_joker(self):
        card_deck = self.api_logic.A_brand_new_deck(jokers_enabled=True)
        self.assertTrue(card_deck['success'])
        self.assertFalse(card_deck['shuffled'])
        self.assertEqual(card_deck['remaining'],54)

    def test_check_card_shuffle(self):
        card_deck = self.api_logic.Shuffle_the_Cards()
        self.assertTrue(card_deck['success'])
        self.assertTrue(card_deck['shuffled'])
        self.assertEqual(card_deck['remaining'], 52)

    def test_if_cards_are_unique(self):
        card_deck = self.api_logic.A_brand_new_deck(jokers_enabled=True)
        deck_id = card_deck['deck_id']
        deck_remaining_card = card_deck['remaining']
        card_deck = self.api_logic.draw_a_card(deck_id, count=deck_remaining_card)
        self.assertTrue(card_deck['success'])
        self.assertEqual(card_deck['remaining'],0)
        self.assertTrue(are_all_cards_in_deck_unique(card_deck['cards']))

    def test_draw_a_card_from_deck(self):
        card_deck = self.api_logic.A_brand_new_deck()
        deck_id = card_deck['deck_id']
        deck_remaining_card = card_deck['remaining']
        card_deck = self.api_logic.draw_a_card(deck_id,count = 5)
        self.assertEqual(deck_remaining_card - 5,card_deck['remaining'])

    def test_return_card_to_deck(self):
        card_deck = self.api_logic.A_brand_new_deck()
        deck_id = card_deck['deck_id']
        deck_remaining_card = card_deck['remaining']
        new_card_deck = self.api_logic.draw_a_card(deck_id,count = deck_remaining_card)
        new_deck_remaining_card = new_card_deck['remaining']
        restored_deck = self.api_logic.return_cards_to_deck(deck_id)
        restored_deck = self.api_logic.get_card_by_id(restored_deck['deck_id'])
        self.assertEqual(0, new_deck_remaining_card)
        self.assertEqual(restored_deck, card_deck)

    def test_adding_card_to_new_deck(self):
        card_deck = self.api_logic.A_brand_new_deck()
        deck_id = card_deck['deck_id']
        shuffled_cards = self.api_logic.shuffle_card_by_id(deck_id)
        shuffled_deck_id = shuffled_cards['deck_id']
        restored_deck = self.api_logic.get_card_by_id(shuffled_deck_id)
        self.assertNotEqual(restored_deck, card_deck)


