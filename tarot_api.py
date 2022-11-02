""" Makes calls to Tarot Card API, get random tarot card """
import requests


def get_tarot_card():
    # get a tarot card (at random) for the user, which includes card name & meaning
    tarot_url = "https://rws-cards-api.herokuapp.com/api/v1/cards/random?n=1"
    response = requests.get(tarot_url)
    tarot_data = response.json()

    tarot_card_name = get_tarot_name(tarot_data)
    tarot_card_meaning = get_tarot_meaning(tarot_data)

    full_tarot_card = [tarot_card_name, tarot_card_meaning]

    # for testing
    print(full_tarot_card)

    return full_tarot_card


def get_tarot_name(tarot_data):
    #gets card name from API
    tarot_card = tarot_data['cards']
    for i in tarot_card:

        card_name = (i['name'])

    return card_name


def get_tarot_meaning(tarot_data):
    #gets the card meaning from API
    tarot_card = tarot_data['cards']
    for i in tarot_card:
        
        card_meaning = (i['meaning_up'])
    
    return card_meaning


get_tarot_card()