def main():
    get_user_info()

def get_user_info():
    user_name = input('What is your name, wonderer?: ')

    list_of_signs = '''
    Aries—March 21-April 19

    Taurus—April 20-May 20

    Gemini—May 21-June 20

    Cancer—June 21-July 22

    Leo—July 23-August 22

    Virgo—August 23-September 22

    Libra—September 23-October 22

    Scorpio—October 23-November 21

    Sagittarius—November 22-December 21

    Capricorn—December 22-January 19

    Aquarius—Jan 20-February 18

    Pisces—February 19-March 20
________________________________________
'''
    print(list_of_signs)
    user_sign = input(f'Please tell me your zodiac sign, {user_name}:').lower

    return user_name, user_sign

if __name__ == '__main__':
    main()