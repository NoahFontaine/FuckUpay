from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from credentials import username, password

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

events = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "EventBookings.EventsList.Load()")]'))
)
events.click()

formal = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "EventBookings.EventsList.Continue(6)")]'))
)
formal.click()


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
