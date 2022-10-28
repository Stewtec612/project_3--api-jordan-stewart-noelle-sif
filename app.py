from flask import Flask, render_template, request

# import API manager module 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/mystic_fetcher')
def mystic_results():
    birthday = request.args 
    print(birthday)

    # what was the user's birthday?
    year = birthday.get('year')
    month = birthday.get('month')
    
    # talk to apis
    # for example, api returns your spirit animal is zebra your horoscope is you will have a nice day 
    # this is example data, replace with data from the API 
    animal = 'zebra'
    horoscope = 'you will have a nice day'
    animal_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Plains_Zebra_Equus_quagga.jpg/1024px-Plains_Zebra_Equus_quagga.jpg'

    # create new web page with results 
    return render_template('results.html', animal=animal, horoscope=horoscope, animal_image_url=animal_url)


if __name__ == '__main__':
    app.run()