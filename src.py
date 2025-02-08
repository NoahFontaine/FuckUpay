from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up WebDriver for Edge
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

print(driver)

# Open the ticket site
driver.get('https://www.upay.co.uk/app/')

print(driver.title)

# Find and interact with form elements (e.g., for selecting tickets)
ticket_button = driver.find_element(By.XPATH, '//button[@id="buy-ticket"]')
ticket_button.click()

# Fill out payment and personal info (Example: Email)
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('your-email@example.com')

# Submit the form (complete purchase)
submit_button = driver.find_element(By.XPATH, '//button[@id="submit-order"]')
submit_button.click()

# Close browser after completing task
driver.quit()

login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
login_button.click()

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('your_username')
password.send_keys('your_password')

login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
login_button.click()

while True:
    if is_ticket_available():  # Define this function to check ticket availability
        buy_ticket()
        break
    time.sleep(5)  # Wait for 5 seconds before checking again
