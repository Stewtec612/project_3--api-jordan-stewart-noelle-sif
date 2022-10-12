import requests
from pprint import pprint

def get_power_animal():
    power_animal_url = 'https://zoo-animal-api.herokuapp.com/animals/rand'

    # todo error handling
    response = requests.get(power_animal_url)

    data = response.json()

    print(data)

    power_animal_name = data['name']
    image_link = data['image_link']  # todo return this too 

    return power_animal_name 


def main():
    animal = get_power_animal()
    print(f'your power animal is: {animal}')


if __name__ == '__main__':
    main()

