"""
Connect to Horoscope API and get the user's horoscope for their sign 
"""


import requests
# import users_sign  # this is unused. Tell the module what the user's sign is
# when you call a function to request their horoscope 

# this needs to go in a function. Almost all your code should be in functions 
# so it can be re-used for different star signs 
# also, so you can test it 
# global variables are hard to test, and there's no way to modify the horoscope_url once created

# #opens channel to the horoscope API
# horoscope_url = f'https://ohmanda.com/api/horoscope/{users_sign}'

# response = requests.get(horoscope_url)

# horoscope_data = response.json()

# really important to use functions so can use code multiple times 
def get_horoscope(users_sign):
    horoscope_url = f'https://ohmanda.com/api/horoscope/{users_sign}'
    response = requests.get(horoscope_url)
    horoscope_data = response.json()
    # TODO deal with errors 
    time = get_time_of_horoscope(horoscope_data)
    details = get_horoscope_details(horoscope_data)
    return time, details  # TODO is this an ok format to return data? Review as team 


def get_time_of_horoscope(horoscope_data):   # be specfic with function names 
    #gets the current date from API
    the_date = horoscope_data['date']
    return the_date


def get_horoscope_details(horoscope_data):
    #gets users horoscope details from the API based off their input of their sign
    users_horoscope = horoscope_data['horoscope']
    return users_horoscope


# just for unofficial testing as this module is being developed
# the app will import this moddule and call get_horoscope and then do whatever you need 
# with the response
if __name__ == '__main__':
    time, scope = get_horoscope('scorpio')
    print(time, scope)
