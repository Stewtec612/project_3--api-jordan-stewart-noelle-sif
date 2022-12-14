"""Recieving the request from the user. Use Request.args.get to retrieve information
ask the seperate module to request the data"""
from flask import Flask, render_template, request
from fate_store import Fate, FateStore

from apis.animal_api import get_animal
from apis.horoscope_api import get_horoscope
from apis.tarot_api import get_tarot_card
# import API manager module 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/mystic_fetcher')
def mystic_results():

    # what was the user's zodiac
    print('form data is', request.args)
    user_zodiac = request.args.get('zodiac') # gets the star sign that was selected by user
    print(user_zodiac)
    # talk to apis
    # for example, api returns your power animal is zebra your horoscope is you will have a nice day 
    # this is example data, replace with data from the API 

    full_animal_info = get_animal()
    horoscope = get_horoscope(user_zodiac)
    
    full_tarot_info = get_tarot_card()


    # # TODO for testing
    # animal_name = 'cheetah'
    # horoscope = 'this is a test horoscope'
    # animal_image_url = 'https://www.washingtonian.com/wp-content/uploads/2022/04/fox-us-capitol.jpg'
    # tarot_card_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/RWS_Tarot_00_Fool.jpg/255px-RWS_Tarot_00_Fool.jpg'

    # create new web page with results 
    return render_template('results.html', animal_name=full_animal_info[0], horoscope=horoscope, animal_image_url=full_animal_info[1], tarot_card_name=full_tarot_info[0],tarot_card_meaning=full_tarot_info[1])


@app.route('/save_fate', methods=['POST'])
def save_fate():
    print('save fate request data:', request.form) # what do you have here? 

    # edit the following line to use data from the request
    fate = Fate(zodiac=mystic_results.zodiac, tarot_card=mystic_results.tarot_card, animal=mystic_results.animal_name, horoscope=mystic_results.horoscope)
    FateStore._save_fate(fate)

    # TODO important you need to return a respose. 
    # Render a new template with all the saved fates, redirect to the home page, whatever you want to do 
    return redirect('/') # change this to whatever you want - currently returns user to home page


if __name__ == '__main__':
    app.run()