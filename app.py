"""Recieving the request from the user. Use Request.args.get to retrieve information
ask the seperate module to request the data"""
from flask import Flask, render_template, request
from fate_store import _get_all_fates

from animal_api import animal_name_request, animal_picture_request
from horoscope_api import horoscope_data
from tarot_api import tarot_card
# import API manager module 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/mystic_fetcher')
def mystic_results():
    zodiac = request.args.get('fates') 
    print(zodiac)

    # what was the user's zodiac
    print('form data is', request.args)
    zodiac = zodiac.get('zodiac')

    # talk to apis
    # for example, api returns your spirit animal is zebra your horoscope is you will have a nice day 
    # this is example data, replace with data from the API 
    animal_name = request.args.get('name')
    animal_pic = request.args.get('pic')
    horoscope = request.args.get('horoscope')
    tarot = tarot_card.get('tarot_data')

    # create new web page with results 
    return render_template('results.html', animal_name=animal_name, horoscope=horoscope, animal_image_url=animal_url)


if __name__ == '__main__':
    app.run()