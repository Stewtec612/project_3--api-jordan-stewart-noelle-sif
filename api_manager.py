""" Manage API information. Get API information from individual API modules, send packaged results to user_interface """
import tarot_api
import animal_api
import horoscope_api
from fate_store import Fate
from get_user_info import get_user_info

zodiac_sign = get_user_info()[1]

card_meaning = tarot_api.get_tarot_meaning()   
card_name = tarot_api.get_tarot_name()   
animal_name = animal_api.get_animal_name()
animal_picture = animal_api.get_animal_picture()
horoscope = horoscope_api.get_horoscope_details()
time = horoscope_api.get_time_of_horoscope()

api_data = {}


def main():

    api_data.update({"Cards Name": card_name,"Tarot Card Meaning": card_meaning, "Animals Name": animal_name,
    "Animal's Picture": animal_picture, "Time": time, "Users Horoscope": horoscope})

    return api_data

def to_db():

    animal = [animal_name, animal_picture]
    tarot_card = [card_meaning, card_name]
    return Fate(animal, tarot_card, horoscope, zodiac_sign)
    