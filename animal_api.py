""" Makes calls to animal API, pulls a random animal """
import requests


def get_animal():
    try:
        # get an animal (at random) for the user, which includes the name & a picture
        animal_url = "https://zoo-animal-api.herokuapp.com/animals/rand"
        response = requests.get(animal_url)
        response.raise_for_status()
        animal_data = response.json()

        animal_picture = get_animal_picture(animal_data)
        animal_name = get_animal_name(animal_data)
        full_animal_info = [animal_name, animal_picture]

        # for testing - currently just shows the link to the animal pic in the terminal
        print(full_animal_info)

        return full_animal_info,None
    except Exception as ex:
        print(ex)
        return None,ex

def get_animal_picture(animal_data):
    #grabs the animal picture link from the API
    animal_picture = animal_data['image_link']
    if animal_picture is None:
        return None
    else:
        return animal_picture


def get_animal_name(animal_data):
    #grabs the animals name from the API
    animal_name = animal_data['name']
    if animal_name is None:
        return None
    
    else:
        return animal_name
    
def main():
    get_animal()

if __name__ == '__main__':
    main()