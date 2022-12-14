""" Manage API information. Get API information from individual API modules, send packaged results to user_interface """
import apis.tarot_api as tarot_api
import apis.animal_api as animal_api
import apis.horoscope_api as horoscope_api
from fate_store import Fate
from get_user_info import get_user_sign


def api_dictionary(user_sign):
    api_data = {}

    api_data.update({"Cards Name": tarot_api.get_tarot_card()[0],"Tarot Card Meaning": tarot_api.get_tarot_card()[1], "Animal's Name": animal_api.get_animal()[0],
    "Animal's Picture": animal_api.get_animal()[1], "Time":horoscope_api.get_horoscope(user_sign)[0], "Users Horoscope": horoscope_api.get_horoscope(user_sign)[1]})

    return api_data


def create_fate_object(user_sign):

    zodiac_sign = user_sign
    tarot_card = tarot_api.get_tarot_card()
    animal = animal_api.get_animal()
    horoscope = horoscope_api.get_horoscope(user_sign)
    
    return Fate(zodiac_sign, tarot_card, animal, horoscope)
    
    