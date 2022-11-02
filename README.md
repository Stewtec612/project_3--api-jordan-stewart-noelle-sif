# project_3--api-jordan-stewart-noelle-sif

Name: Mystic Fate Fortune 

Project Description: A user can enter their birthdate & receive a 'Mystic Fate', which gives them their horoscope, a spirit animal, & draws a tarot card for them.
    They can save this information to the fate-store, for later reference.


Instructions for Installation: 
    Use 'pip install' for all requirements 
   
Set up Flask Evnviornment 
pip install flask

![Requirements](readme_images/requirements.png)

### Example Output 
![CMD output](readme_images/cmd_run.png)
![UI output](readme_images/webUI.png)


### Errors
![ErrSaveFate](readme_images/error_savefate.png)
![ErrUI](readme_images/err_ui.png)

### APIs:
    Tarot Card
    Animal
    Horoscope

### FUNCTIONS:
def save_mystic_data(): --> (card, animal, & horoscope -- attached to a user?)
get_mystic_fate(): This function will draw a random card, random animal, & your horoscope
    It asks for user's birth day to pull correct horoscope tied to star sign
    It will assign numbers to get a random id / animal
get_random_tarot():
    tarot card can pull
get_random_animal():
    use a random number generator to grab an animal with that 'random' ID, and return it.
get_starsign_horoscope(birthdate):
    take users birthdate & return horoscope based on their star sign.

### MODULES:
tarot_card_api
animal_api
horoscope_api
Mystic Fate Results (peewee/sqlite)
User Interface (Html, js, css)
Fate_Store --> store results (send results objects to the fate_store, retrieve list of past saved 'fate' objects)
    fate object holds: (tarot_card, animal, horoscope)
Api_Manager (receives results, sends them to the individual API modules?)
    Taking the results and sends it back to the user interface 
User_interface
    ** fate object -- variable
    **Presents information to the user
Manager (receives requests or problems from the user_interface)



Uses SQLite3 database to store data. 

Requires at least Python 3.7.


