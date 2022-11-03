""" Makes calls to Tarot Card API, get random tarot card """
import requests


def get_tarot_card():
    '''
    Function is in charge of requesting a random tarot card from the tarot card api and to select the name and meaning from the json object response
    '''
    try:
        # get a tarot card (at random) for the user, which includes card name & meaning
        tarot_url = "https://rws-cards-api.herokuapp.com/api/v1/cards/random?n=1"
        response = requests.get(tarot_url)
        response.raise_for_status()
        tarot_data = response.json()

        tarot_card_name = get_tarot_name(tarot_data)
        tarot_card_meaning = get_tarot_meaning(tarot_data)

        full_tarot_card = [tarot_card_name, tarot_card_meaning]

        return full_tarot_card, None
    
    except Exception as ex:
        print(ex)
        return None,ex
        # for testing
        #print(full_tarot_card)

    return full_tarot_card


def get_tarot_name(tarot_data):
    '''
    incharge of selecting the name from the json object
    '''
    #gets card name from API
    tarot_card = tarot_data['cards']
    for i in tarot_card:

        card_name = (i['name'])
        if card_name is None:
            return None
        else:
            return card_name


def get_tarot_meaning(tarot_data):
    '''
    incharge of selecting the meaning from the json object
    '''
    #gets the card meaning from API
    tarot_card = tarot_data['cards']
    for i in tarot_card:
        
        card_meaning = (i['meaning_up'])
        if card_meaning is None:
            return None
        else:
            return card_meaning


#for testing
# def main():
#     get_tarot_card()

# if __name__ == '__main__':
#     main()