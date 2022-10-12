import requests
from pprint import pprint

def get_horoscope_for_sign(users_sign):
    horoscope_url = f'https://ohmanda.com/api/horoscope/{users_sign}'

    # todo error handling
    #  One kind of error is can't connect to site, server down 
    #  Another kind of error is entering an invalid sign - what does the API do if users_sign is "" or "qwerty"
    
    response = requests.get(horoscope_url)

    data = response.json()

    date = data['date']
    zodiac_sign = data['sign']
    horoscope = data['horoscope']

    print(f'Today\'s date: {date}\n')
    print(f'Zodiac sign: {zodiac_sign}\n')
    pprint(horoscope)

    return horoscope   # TODO what should this function return? Just the text horoscope, 
    # or should it return other data too? 


# for developement and verifying functionality from the command prompt
def main():
    users_sign = input('enter your zodiac sign: ').lower()
    horoscope = get_horoscope_for_sign(users_sign)
    print(horoscope)

# if this file is run from the terminal, main gets called - so you can run this file in isolation for testing
# if this file is imported from another module main does NOT get called - so the appliation can import the file
if __name__ == '__main__':
    main()




