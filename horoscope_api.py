""" Make calls to Horoscope API, get horoscope based on the user's sign """

import requests


def get_horoscope(user_sign):
    try:

        user_sign = user_sign.lower()
        # get a user horoscope based of the user's sign, that includes the date of the horoscope
        horoscope_url = f'https://ohmanda.com/api/horoscope/{user_sign}'
        response = requests.get(horoscope_url)
        response.raise_for_status()
        print(response)
        horoscope_data = response.json()
        time = get_time_of_horoscope(horoscope_data)
        details = get_horoscope_details(horoscope_data)
        full_horoscope = [time, details]

        return full_horoscope,None
    
    except Exception as ex:
        print(ex)   #prints raised status of api url
        return None,ex
    
    


        # for testing - we will still make some changes for formatting for the user
        # print(full_horoscope)
        
        

def get_time_of_horoscope(horoscope_data):
    # gets the current date from API
    the_date = horoscope_data['date']
    if the_date is None:
        return None
    else:
        return the_date


def get_horoscope_details(horoscope_data):
    # gets users horoscope details from the API based off their input of their sign
    users_horoscope = horoscope_data['horoscope']
    if users_horoscope is None:
        return None

    return users_horoscope

    #get_horoscope(user_sign)

# for testing during development
# if __name__ == '__main__':
#     time, scope = get_horoscope('scorpio')
#     print(time, scope)