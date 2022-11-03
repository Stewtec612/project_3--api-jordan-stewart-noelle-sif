""" Makes calls to animal API, pulls a random animal """
import requests


def get_animal():
    '''
    this function is in charge of making requests to the random animal api url and select the name and picture out of the json object
    '''
    try:
        # get an animal (at random) for the user, which includes the name & a picture
        animal_url = "https://zoo-animal-api.herokuapp.com/animals/rand"
        response = requests.get(animal_url)
        response.raise_for_status()
        animal_data = response.json()

        animal_picture = get_animal_picture(animal_data)
        animal_name = get_animal_name(animal_data)
        full_animal_info = [animal_name, animal_picture]

        return full_animal_info, None
    except Exception as ex:
        print(ex)#prints raised status of api url
        return None,ex

def get_animal_picture(animal_data):
    '''
    In charge of selecting animal picture out of json object
    '''
    #grabs the animal picture link from the API
    animal_picture = animal_data['image_link']
    if animal_picture is None:
        return None
    else:
        return animal_picture
      
def get_animal_name(animal_data):
    '''
    in charge of selecting the animal name out of json object
    '''
    #grabs the animals name from the API
    animal_name = animal_data['name']
    if animal_name is None:
        return None
    
    else:
        return animal_name
      
#for testing
        
# def main():
#     get_animal()

# if __name__ == '__main__':
#     main()

