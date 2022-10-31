""" Manage API information. Get API information from individual API modules, send packaged results to user_interface """
import tarot_api
import animal_api
import horoscope_api
from fate_store import Fate
from get_user_info import get_user_info

zodiac_sign = get_user_info()[1]

card_meaning = tarot_api.tarot_meaning_request()   
card_name = tarot_api.tarot_name_request()   
animal_name = animal_api.animal_name_request()
animal_picture = animal_api.animal_picture_request()
horoscope = horoscope_api.horoscope_details()
time = horoscope_api.time()

api_data = {}


def main():

    api_data.update({"Cards Name": card_name,"Tarot Card Meaning": card_meaning, "Animals Name": animal_name,
    "Animal's Picture": animal_picture, "Time": time, "Users Horoscope": horoscope})

    return api_data

def to_db():

    animal = [animal_name, animal_picture]
    tarot_card = [card_meaning, card_name]
    return Fate(animal, tarot_card, horoscope, zodiac_sign)
    