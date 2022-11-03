from fate_store import Fate
import api_manager
import get_user_info
import horoscope_api
import animal_api

def main(): 
    
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
        get_user_horoscope()
        get_animal()

        
        
        # save_response = input('would you like to save your fate? y/n: ').lower
        # if save_response == 'y':
        #     save_fate()
        # else:
        #     main()


        

def get_user_horoscope():
    user_sign = get_user_info.get_user_sign()

    new_fate = api_manager.create_fate_object(user_sign)


def get_animal():
    #animal_data = animal_api.get_animal()
    animal_name = animal_api.get_animal()
    print(f'\nyour power animal is: {animal_name}\n')



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