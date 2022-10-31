# import get_user_info
# from main import display_all_fates  # does this cause an error? Circular import?

# def display_user_options():
#     while True:
#         try:
#             options = ''' 
#             1) Generate New Fate
#             2) Display Saved Fates
#             3) Quit
#             '''
#             print(options)
#             user_choice = input('choose an option: ')

#             if user_choice == '1':
#                 get_user_info.get_user_info()
#             if user_choice == '2':
#                 display_all_fates()
#             if user_choice == '3':
#                 break
#             else:
#                 print('Not a valid selection, enter a number from 1-3.')
#         except:
#             print('Error.')

