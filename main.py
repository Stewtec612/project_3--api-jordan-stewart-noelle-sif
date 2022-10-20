from fate_store import Fate
import fate_store

def main(): 
    menu_text = '1. Today\'s Fate 2. Display Past Fates 3. Quit'
    print(menu_text)

    while True:
        choice = input('Enter a choice: ')
        if choice == '1':
            generate_new_fate()
        elif choice == '2':
            display_all_fates()
        elif choice == '3':
            break
        else:
            print('Not a valid selection, please try again')


def generate_new_fate():
    print('todo ')
    # todo potentially break down into further functions

    zodiac_list = ["Aries—March 21-April 19",
        "Taurus—April 20-May 20",
        "Gemini—May 21-June 20",
        "Cancer—June 21-July 22",
        "Leo—July 23-August 22",
        "Virgo—August 23-September 22",
        "Libra—September 23-October 22",
        "Scorpio—October 23-November 21", 
        "Sagittarius—November 22-December 21",
        "Capricorn—December 22-January 19",
        "Aquarius—Jan 20-February 18",
        "Pisces—February 19-March 20"]


    def get_horoscope():
        """ # needs to ask for user input (zodiac sign)
        # needs to make calls to tarot (random), animal (random), & horoscope (user input zodiac) apis
        # needs to gather this information """


        print('todo get user zodiac input, make call to horoscope API, and add to Fate object')
        print(zodiac_list)
        zodiac = input('Please enter your zodiac sign from the list: ')

        # use zodiac to make api call


    def get_tarot():
        print('todo make call to api and get random tarot card, add to Fate object')


    def get_animal():
        print('todo make call to api and get random tarot card, add to Fate object')


    def display_fate():
        """ Display the Fate object for user, and ask them in they wish to save it """
        print('todo display the user fate for them, and ask them if they want to save it.')
        save_response = input('Enter 1 if you would like to save your newly generated Fate, or 2 if you wish to delete.')

        if save_response == 1:
            save_fate()

def display_all_fates():
    print('todo display all Fates the user has saved')
    # call DB/fate_store's view_all_fates() function
    Fate.view_all_fates()


def save_fate():
    print('todo save fate into the DB. Call save() db method')
    # call DB / fate_store's
    fate_store.save()

if __name__ == '__main__':
    main()