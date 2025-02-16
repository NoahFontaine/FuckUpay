# Fuck UPay

## How to use:

### Create a virtual enviroment for all your dependencies:
1. Open the **pyproject.toml** file to see the required dependencies.
2. Install your venv and dependencies in however way you want.

### Input your user login credentials:
1. Create a python file called **credentials.py** in the **src/** directory.
2. This file must only be comprised of 2 lines:
    > username = 'CRSid@cam.ac.uk' <br>
    > password = 'yourPassword'


### Go on src/main.py and:
1. Enter the event you want to attend in the my_event variable. You can only choose between the events in the events dictionary.
2. Enter the names of your guests in the **guests** list. Each guest is a list in itself, nested in that list. Each guest must be entered in the form ['Title', 'First Name Last Name'].
3. Enter the menus that you and each guest wishes to buy, in **CAPITAL** letters, in the menus list. The first element is the menu of the Pembroke organizer, the rest of the menus must be in the same order as the guests.
4. Enter the date of the event in the form 'DDth Mon YYYY' (Eg: 16th Feb 2025). Make sure to include the 'th', 'st', 'nd', or 'rd' after the 'DD', depending on the date.
5. Run the **main.py** script!