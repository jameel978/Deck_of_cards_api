from Infra.api_wrapper import APIWrapper


class DeckOfCards:
    URL = "https://deckofcardsapi.com/"
    def __init__(self,api_object):
        self.my_api = api_object

    def Shuffle_the_Cards(self,count = 1):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/new/shuffle/?deck_count={count}')
        return result.json()
            
    def draw_a_card(self,card_id,count):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/{card_id}/draw/?count={count}')
        return result.json()
        
    def reshuufle_the_cards(self,card_id,remaining = False):
        #https://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/    
        my_api = APIWrapper()
        if remaining:
            my_api_address = f'{self.URL}api/deck/{card_id}/shuffle/?remaining=true'
        else: 
            my_api_address = f'{self.URL}api/deck/{card_id}/shuffle/'
        result = my_api.api_get_request(my_api_address)
        return result.json()   
    
    def A_brand_new_deck(self,jokers_enabled=False):
        my_api = APIWrapper()
        if jokers_enabled:
            my_api_address = f'{self.URL}api/deck/new/?jokers_enabled=true'
        else:
            my_api_address = f'{self.URL}api/deck/new/'
        result = my_api.api_get_request(my_api_address)
        return result.json() 

    def return_cards_to_deck(self,card_id):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/{card_id}/return/')
        return result.json()

    def get_card_by_id(self,card_id):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/{card_id}/')
        return result.json()


    def shuffle_card_by_id(self,card_id):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/{card_id}/shuffle/')
        return result.json()

    def add_to_piles(self,card_id,pile_name,card_codes):
        #https://deckofcardsapi.com/api/deck/%3C%3Cdeck_id%3E%3E/pile/%3C%3Cpile_name%3E%3E/add/?cards=AS,2S
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/{card_id}/pile/{pile_name}/add/?cards={card_codes}')
        return result.json()

    def draw_from_pile(self,card_id,pile_name,card_codes):
        #https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/draw/?count=2
        my_api = APIWrapper()
        result = my_api.api_get_request(f'{self.URL}api/deck/{card_id}/pile/{pile_name}/draw/?cards={card_codes}')
        return result.json()