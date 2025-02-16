from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from credentials import username, password


def login_and_navigate(event_number: str,
                       date: str,
                       guests: list[list[str]],
                       menus: list[str]
                       ):
    
    # Set up WebDriver for Edge
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    # Open the ticket site
    driver.get('https://www.upay.co.uk/app/')

    # Fill out payment and personal info (Example: Email)
    email_field = driver.find_element(By.ID, 'txtUsername')
    email_field.send_keys(username)

    password_field = driver.find_element(By.ID, 'txtPassword')
    password_field.send_keys(password)

    login = driver.find_element(By.ID, 'btnLogin')
    login.click()

    menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'divChilliHeaderMenuToggle'))
    )
    menu.click()

    # Retry logic for clicking the events element
    for _ in range(3):  # Retry up to 3 times
        try:
            events = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "EventBookings.EventsList.Load()")]'))
            )
            events.click()
            break  # Exit loop if click is successful
        except Exception as e:
            print(f"Retrying due to: {e}")
            sleep(2)  # Wait before retrying

    while True:
        try:
            formal = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[contains(@onclick, "EventBookings.EventsList.Continue({event_number})")]'))
            )
            formal.click()
            break
        except:
            print('need to press ok element')
            ok_button = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-button') and contains(@class, 'pop-up-bottom')]")
            
            ok_button.click()

    date_popup = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "EventBookings.EventDates.ChooseDates()")]'))
    )
    date_popup.click()

    # Locate the div with "27th Feb 2025"
    date_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'date-list--date')][contains(., '{date}')]"))
    )
    
    date_element.click()

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "Modal.Close(EventBookings.EventDates.OnDatesSelected)")]'))
    )
    continue_button.click()

    # add_guest_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, 'btnAddGuest'))
    # )
    # add_guest_button.click()
    for menu in menus:
        menu_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{menu}')]"))
        )
        menu_button = menu_element.find_element(By.XPATH, "./ancestor::li[contains(@class, 'eb--category-item')]//div[contains(@class, 'btn-check')]")
        print('scrolling to button')
        # Scroll to the button and click it
        try:
            menu_button.click()
        except:
            driver.execute_script("arguments[0].scrollIntoView(true);", menu_button)
            print('scrolled to button')
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(menu_button))
            menu_button.click()

    # # .... #
    # for guest in guests:
    #     food_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, f'/html/body/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div/ul/li[3]/div[1]/div/div'))
    #     )

    # yes = str(input('Do you want to continue? (y/n): '))
    # if yes == 'y':
    # Scroll to the specific element
    to_payout = driver.find_element(By.ID, 'btn btn-grey')
    driver.execute_script("arguments[0].scrollIntoView();", to_payout)

    to_payout.click()


    sleep(300)


    # Close browser after completing task

    driver.quit()


# login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
# login_button.click()

# username = driver.find_element(By.NAME, 'username')
# password = driver.find_element(By.NAME, 'password')

# username.send_keys('your_username')
# password.send_keys('your_password')

# login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
# login_button.click()

# while True:
#     if is_ticket_available():  # Define this function to check ticket availability
#         buy_ticket()
#         break
#     time.sleep(5)  # Wait for 5 seconds before checking again
