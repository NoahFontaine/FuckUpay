from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def login(username, password):
    # Set up WebDriver for Edge
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    # Open UPay
    driver.get('https://www.upay.co.uk/app/')

    email_field = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, 'txtUsername'))
    )
    email_field.send_keys(username)

    password_field = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, 'txtPassword'))
    )
    password_field.send_keys(password)

    login = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.ID, 'btnLogin'))
    )
    login.click()

    return driver


def navigate_and_buy(driver: webdriver.Edge,
                     event_number: str,
                     date: str,
                     guests: list[list[str]],
                     menus: list[str]
                     ):
    

    menu = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "Menu.ToggleTopMenu()")]'))
    )
    menu.click()

    for _ in range(3):
        try:
            events = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "EventBookings.EventsList.Load()")]'))
            )
            events.click()
            break  # Exit loop if click is successful
        except Exception as e:
            print(f"Retrying due to: {e}")
            sleep(2)  # Wait before retrying

    while True:
        try:
            formal = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[contains(@onclick, "EventBookings.EventsList.Continue({event_number})")]'))
            )
            formal.click()

            date_popup = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "EventBookings.EventDates.ChooseDates()")]'))
            )
            date_popup.click()

            break
        except:
            print('need to press ok element')
            ok_button = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-button') and contains(@class, 'pop-up-bottom')]")
            
            ok_button.click()

    date_element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'date-list--date')][contains(., '{date}')]"))
    )

    while True:
        try:
            date_element.click()
            break
        except Exception as e:
            print(f"Retrying due to: {e}")
            sleep(0.05)  # Wait for 0.05 seconds before retrying (20 times per second)

    continue_button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "Modal.Close(EventBookings.EventDates.OnDatesSelected)")]'))
    )
    continue_button.click()

    ### Uncomment and test this section to add guests ###
    '''
    if len(guests) ! == 0:
        for guest in guests:
            add_guest = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@onclick, "EventBookings.EventGuests.ShowAddGuestModal()")]'))
            )
            add_guest.click()

            title = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, 'txtGuestTitle'))
            )
            title.send_keys(guest[0])

            name = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, 'txtGuestName'))
            )
            name.send_keys(guest[1])

            name = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, 'txtGuestName'))
            )
            name.send_keys(guest[1])

            add_guest = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, 'btnAddGuest'))
            )
            add_guest.click()
    '''


    ### Uncomment and test this section to add menus, making sure the menus are different ###
    '''
    for menu in menus:
        menu_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{menu}')]"))
        )
        menu_button = menu_element.find_element(By.XPATH, "./ancestor::li[contains(@class, 'eb--category-item')]//div[contains(@class, 'btn-check')]")
        print('scrolling to button')
        # Scroll to the button and click it
        try:
            menu_button.click()
        except:
            driver.execute_script("arguments[0].scrollIntoView(true)", menu_button)
            print('scrolled to button')
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(menu_button))
            menu_button.click()
    '''

    
    to_payout = driver.find_element(By.XPATH, '//button[contains(@onclick, "EventBookings.EventHub.Continue()")]')
    driver.execute_script("arguments[0].scrollIntoView()", to_payout)

    to_payout.click()

    ######## UNCOMMENT THIS SECTION TO BUY THE TICKET(S) ########
    '''
    # Buy the ticket(s)
    buy_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@onclick, "EventBookings.Review.Continue()")]'))
    )
    buy_button.click()
    '''

    sleep(300)


    driver.quit()
