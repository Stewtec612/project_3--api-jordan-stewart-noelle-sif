def main():
    get_user_name()
    get_user_sign()

def get_user_name():
    user_name = input('What is your name, wonderer? ')
    
    return user_name

def get_user_sign():
    while True:
        dict_of_signs ={
        'Aries':'aries',

        'Taurus':'taurus',

        'Gemini':'gemini',

        'Cancer':'cancer',

        'Leo':'leo',

        'Virgo':'virgo',

        'Libra': 'libra',

        'Scorpio':'scorpio',

        'Sagittarius': 'sagittarius',

        'Capricorn':'capricorn',

        'Aquarius':'aquarius',

        'Pisces':'pisces'
        }
        for sign in dict_of_signs:
            print(sign)
        try:
            user_sign = input(f'Please tell me your zodiac sign: ').lower()
            if user_sign not in dict_of_signs.values():
                raise ValueError
        except ValueError:
            print('ERROR: must enter a zodiac sign from the list')
        else:
            return user_sign

if __name__ == '__main__':
    main()