from horoscope_api import get_horoscope_for_sign
from power_animal_api import get_power_animal

# import other API modules 

"""
Make request to all three APIs
"""

def get_mystic_fortune(star_sign):

    horoscope = get_horoscope_for_sign(star_sign)
    animal = get_power_animal()

    # todo call other API

    # return all the data 



# just for testing, not part of regular app 
def main():
    get_mystic_fortune('libra')

if __name__ == '__main__':
    main()

