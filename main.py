from fate_store import Fate
import apis.api_manager as api_manager
import get_user_info
import apis.horoscope_api as horoscope_api
import apis.animal_api as animal_api
import apis.tarot_api as tarot_api

def main(): 
        '''
        in charge of loading a menu with options and derect the program to those objects and back
        '''
    
        mystic_menu = '''
        1.) Fate of Today 
        2.) Display Fates of the Past 
        3.) Decline the Mystic's Wisdom'''
        
        
        while True:
            try:
                print(mystic_menu)
                choice = input('\n Enter a choice: ')
                if choice == '1':
                    generate_new_fate()
                elif choice == '2':
                    display_all_fates()
                elif choice == '3':
                    quit_message()
                    break
                else:
                    raise ValueError
                
            except ValueError:
                print('ERROR: Must select an option between 1-3')


def generate_new_fate():
        '''
        when the user selects option 1, it will ask for their zodiac sign and return the user a horoscope, a power animal, and a tarot card to display and the user has the option to save all of them as 1 sql string
        '''
        user_sign = get_user_info.get_user_sign()
        animal_name = animal_api.get_animal()
        horoscope = horoscope_api.get_horoscope(user_sign)
        tarot_data = tarot_api.get_tarot_card()

        full_fate_dict = {"todays Date: ": horoscope[1], "Your sign: ": user_sign,"Your Horoscope: ": horoscope[0],"your power animal is: ": animal_name[0], "As well as a link to it's image: ": animal_name[1],
        "Your tarot card's name: ": tarot_data[0], "And it's description: ": tarot_data[1] }

        for  x, y in full_fate_dict.items():
            print(x ,y)
        
        
        save_response = input('would you like to save your fate? y/n: ').lower
        if save_response == 'y':
             save_fate()
        else:
             main()


def display_all_fates():
    print('todo display all Fates the user has saved')
    # call DB/fate_store's view_all_fates() function
    Fate.view_all_fates()


def save_fate(new_fate):
    print('Fate Saved')
    # call DB / fate_store's
    # new_fate = api_manager.create_fate_object()
    Fate.save(new_fate)

def quit_message():
    print('\nWhen the planets aline, we shall meet again...\n')



if __name__ == '__main__':
    main()