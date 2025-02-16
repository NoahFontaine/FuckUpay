from navigation_functions import login, navigate_and_buy
from credentials import username, password

################# INPUTS #################

# 1. Enter the event you want to attend.
events = {'Formal': '6',
         'Monday Formal': '13',
         'Engineering Dinner': '28'
         }
my_event = 'Formal'

# 2. Enter the guests you want to invite here.
# Each list element is in the form
# ['Title', 'First Name', 'Last Name'].
guests = [['', '', ''],
          ['', '', ''],
          ['', '', '']]

# 3. Enter the menus you want to select here.
# Each element is a string and in capital letters.
# First menu is for the Pembroke organiser.
menus = ['STANDARD',
         '',
         '',
         '']

# 4. Enter the date of the event you want to attend.
# Format: 'DDth Mon YYYY'.
# Make sure to include the 'th' or 'st' etc.
date = '27th Feb 2025'


##########################################

if __name__ == '__main__':
    guests = [guest for guest in guests if
              (guest[0] != '' or guest[1] != '')]
    menus = [menu for menu in menus if menu != '']


    driver = login(username, password)

    navigate_and_buy(driver, events[my_event], date,
                    guests, menus)