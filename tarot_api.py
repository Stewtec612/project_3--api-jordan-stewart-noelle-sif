import requests
#Opens channel to the a tarot card API
tarot_url = "https://rws-cards-api.herokuapp.com/api/v1/cards/random?n=1"

response = requests.get(tarot_url)

tarot_data = response.json()

tarot_card = tarot_data['cards']


def tarot_name_request():
    #gets card name from API
    for i in tarot_card:

        card_name = (i['name'])

    return card_name


def tarot_meaning_request():
    #gets the cards meaning from API
    for i in tarot_card:
        
        card_meaning = (i['meaning_up'])
    
    return card_meaning

