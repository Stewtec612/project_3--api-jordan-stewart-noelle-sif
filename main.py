from fate_store import Fate
import api_manager
from get_user_info import get_user_name, get_user_sign

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
    get_user_name()
    user_sign = get_user_sign()


    """ Display the Fate object for user, and ask them in they wish to save it """
    print("\n".join("{}\t{}".format(k, v) for k, v in api_manager.api_dictionary(user_sign).items()))
    save_response = input('would you like to save your fate? y/n: ')

    new_fate = api_manager.create_fate_object(user_sign)


    if save_response.lower() == 'y':
        save_fate(new_fate)
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



if __name__ == '__main__':
    main()