""" Manage API information. Get API information from individual API modules, send packaged results to user_interface """
import tarot_api
import animal_api
import horoscope_api
from fate_store import Fate
from get_user_info import get_user_info

api_data = {}


def api_dictionary():

    api_data.update({"Cards Name": tarot_api.get_tarot_name(),"Tarot Card Meaning": tarot_api.get_tarot_meaning(), "Animals Name": animal_api.get_animal_name(),
    "Animal's Picture": animal_api.get_animal_picture(), "Time":horoscope_api.get_time_of_horoscope(), "Users Horoscope": horoscope_api.get_horoscope_details()})

    return api_data

def create_fate_object():

    animal = animal_api.get_animal()
    tarot_card = tarot_api.get_tarot_card()
    horoscope = horoscope_api.get_horoscope()
    zodiac_sign = get_user_info()[1]

    return Fate(zodiac_sign, tarot_card, animal, horoscope)
    
    