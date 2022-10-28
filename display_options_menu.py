import get_user_info

def main():
    display_user_options()


def display_user_options():
    while True:
        try:
            options = ''' 
            1) Generate New Fate
            2) Display Saved Fates
            3)Quit
            '''
            print(options)
            user_choice = input ('choose an option: ')

            if user_choice == '1':
                get_user_info.get_user_info()
            #if user_choice == '2': insert db display module here
            
            if user_choice == '3':
                break
        
        except:
            print('Must enter a number from 1 - 3')

if __name__ == '__main__':
    main()

