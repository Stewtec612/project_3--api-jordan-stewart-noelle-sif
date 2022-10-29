""" Manage API information. Get API information from individual API modules, send packaged results to user_interface """
import tarot_api
import animal_api
import horoscope_api

card_meaning = tarot_api.tarot_meaning_request()   
card_name = tarot_api.tarot_name_request()   
animal_name = animal_api.animal_name_request()
animal_picture = animal_api.animal_picture_request()
users_horoscope = horoscope_api.horoscope_details()
time = horoscope_api.time()

api_data = {}


def main():

    api_data.update({"Cards Name": card_name,"Tarot Card Meaning": card_meaning, "Animals Name": animal_name,
    "Animal's Picture": animal_picture, "Time": time, "Users Horoscope": users_horoscope})

    return api_data
