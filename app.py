"""Recieving the request from the user. Use Request.args.get to retrieve information
ask the seperate module to request the data"""
# from django.shortcuts import redirect  # ?
from flask import Flask, render_template, request, redirect

"""
 this import doesn't work. fate_store has a class called 
 FateStore and FateStore has an instance method called
 _get_all_fates. So this method only makes sense if you 
 have a FateStore object to call it for. 
"""
# from fate_store import _get_all_fates
from fate_store import Fate, FateStore  # do you want to import the class definition?

from animal_api import animal_name_request, animal_picture_request
# from horoscope_api import horoscope_data  # this isn't working
from tarot_api import tarot_card
# import API manager module 

app = Flask(__name__)

fateStore = FateStore()  # and instantiate a new FateStore that you can call it's methods? 

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/mystic_fetcher')
def mystic_results():
    zodiac = request.args.get('fates') 
    print(zodiac)

    # what was the user's zodiac
    print('form data is', request.args)
    zodiac = request.args.get('zodiac')  # this figures out what star sign was selected 

    # talk to apis
    # for example, api returns your spirit animal is zebra your horoscope is you will have a nice day 
    # this is example data, replace with data from the API 

    # these should be calls to your API, not more request.args.get...
    # animal_name = request.args.get('name')
    # animal_pic = request.args.get('pic')
    # horoscope = request.args.get('horoscope')
    # tarot = request.args.get('tarot_data')
    
    animal_name = 'goldfish' # placeholders to test your page 
    horoscope = 'test horoscope'
    animal_url = 'example.jpg'

    # create new web page with results 
    return render_template('results.html', animal_name=animal_name, horoscope=horoscope, animal_image_url=animal_url)


@app.route('/save_fate', methods=['POST'])
def save_fate():
    print('save fate request data:', request.form) # what do you have here? 
    # edit the following line to use data from the request
    fate = Fate('scorpio', 'you will have a nice day', 'goldfish.png', 'whatever your arguments should be')
    fateStore._save_fate(fate)  #
    # TODO important you need to return a respose. 
    # Render a new template with all the saved fates, redirect to the home page, whatever you want to do 
    return redirect('/') # change this to whatever you want 

if __name__ == '__main__':
    app.run()