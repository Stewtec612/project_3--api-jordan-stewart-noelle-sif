

import requests
# import users_sign  # is this used?
# I remember talking to someone in your group about this code
# is there another version somewhere? 

#opens channel to the horoscope API
# this needs to be in a function, I'm commenting it out to get your app running 
# but you'll need to put something back here
# horoscope_url = f'https://ohmanda.com/api/horoscope/{users_sign}'

# response = requests.get(horoscope_url)

# horoscope_data = response.json()


def temp_example_horoscope_replace_with_real_code(sign):
    return 'today will be a nice day'


def time():
    #gets the current date from API
    the_date = horoscope_data['date']

    return the_date


def horoscope_details():
    #gets users horoscope details from the API based off their input of their sign
    users_horoscope = horoscope_data['horoscope']

    return users_horoscope