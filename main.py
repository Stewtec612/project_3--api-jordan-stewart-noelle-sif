from fate_store import Fate
import api_manager

def main(): 
    menu_text = '1. Today\'s Fate 2. Display Past Fates 3. Quit'
    print(menu_text)

    while True:
        try:
            choice = input('Enter a choice: ')
            if choice == '1':
                generate_new_fate()
            elif choice == '2':
                display_all_fates()
            elif choice == '3':
                break
            else:
                print('Not a valid selection, enter a number from 1-3.')
        except:
            print('Error.')


def generate_new_fate():
    print('generate_new_fate() function -- get rid of?')
    display_fate()


def display_fate():
    """ Display the Fate object for user, and ask them in they wish to save it """
    print("\n".join("{}\t{}".format(k, v) for k, v in api_manager.api_dictionary().items()))
    save_response = input('would you like to save your fate? y/n')

    if save_response.lower() == 'y':
        save_fate()
    else:
        main()


def display_all_fates():
    print('main.display_all_fates() function')
    # call DB/fate_store's view_all_fates() function
    Fate.view_all_fates()


def save_fate():
    print('Fate Saved')
    # call DB / fate_store's save function
    new_fate = api_manager.create_fate_object()
    new_fate.save()



if __name__ == '__main__':
    main()