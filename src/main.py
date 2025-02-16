from my_test import login_and_navigate

guests = [['', ''],
          ['', ''],
          ['', '']]

menus = ['STANDARD',
         '',
         '',
         '']

date = '27th Feb 2025'

events = {'Formal': '6',
         'Monday Formal': '13',
         'Engineering Dinner': '28'
         }

event_I_want_to_go_to = 'Engineering Dinner'


# Remove guests with empty first name and last name
guests = [guest for guest in guests if guest[0] != '' or guest[1] != '']
menus = [menu for menu in menus if menu != '']

login_and_navigate(events[event_I_want_to_go_to], date,
                   guests, menus)