''' TASK: access random zoo animal api and collect the image and name items from the json object '''

import requests
#opens channel to animal API
animal_url = "https://zoo-animal-api.herokuapp.com/animals/rand"

response = requests.get(animal_url)

animal_data = response.json()


def animal_picture_request():
    #grabs the animal picture link from the API
    animal_picture = animal_data['image_link']

    return animal_picture


def animal_name_request():
    #grabs the animals name from the API
    animal_name = animal_data['name']
    
    return animal_name
    



