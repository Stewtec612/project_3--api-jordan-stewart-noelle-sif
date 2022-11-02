""" Manage API information. Get API information from individual API modules, send packaged results to user_interface """
import tarot_api
import animal_api
import horoscope_api
from fate_store import Fate
from get_user_info import get_user_sign


def api_dictionary(user_sign):
    api_data = {}

    api_data.update({"Cards Name": tarot_api.get_tarot_card()[0],"Tarot Card Meaning": tarot_api.get_tarot_card()[1], "Animal's Name": animal_api.get_animal()[0],
    "Animal's Picture": animal_api.get_animal()[1], "Time":horoscope_api.get_horoscope(user_sign)[0], "Users Horoscope": horoscope_api.get_horoscope(user_sign)[1]})

    return api_data


def create_fate_object():

    animal = animal_api.get_animal()
    tarot_card = tarot_api.get_tarot_card()
    horoscope = horoscope_api.get_horoscope()
    zodiac_sign = get_user_sign()

    return Fate(zodiac_sign, tarot_card, animal, horoscope)
    
    