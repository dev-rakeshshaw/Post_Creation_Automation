from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

# Function to prompt the user for input
def get_user_input():
    status = input("Enter status (DF for Draft, PB for Published): ")
    tags = input("Enter tags (comma-separated): ")
    return status, tags

# Get user input for status and tags
status, tags = get_user_input()

# Path to the ChromeDriver executable
chrome_driver_path = "/usr/bin/chromedriver"

service = Service(chrome_driver_path)

# Initializing the WebDriver
driver = webdriver.Chrome(service=service)

# Opening the Django admin login page
driver.get("http://127.0.0.1:8000/admin/")
driver.maximize_window()

# Finding the username and password fields and enter the credentials
username_field = driver.find_element(By.ID, "id_username")
password_field = driver.find_element(By.ID, "id_password")

username_field.send_keys("rakesh")
password_field.send_keys("admin")

# Submitting the form by pressing Enter in the password field
password_field.send_keys(Keys.RETURN)

# Waiting for the page to load completely after login
driver.implicitly_wait(5)  

# Click the "Add" link under the "Posts" section
add_link = driver.find_element(By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/td[1]/a')
time.sleep(2)  # Delay for 2 seconds
add_link.click()

# Waiting for the page to load completely
driver.implicitly_wait(5) 

# Filling in the form fields with a delay
# time.sleep(2)  # Delay for 2 seconds

# Generate a random string of length 10
random_title = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Filling in the form field with the random title
driver.find_element(By.ID, "id_title").send_keys(random_title)

time.sleep(2)  # Delay for 2 seconds
driver.find_element(By.ID, "id_author").send_keys("rakesh")

time.sleep(2)  # Delay for 2 seconds
driver.find_element(By.ID, "id_body").send_keys("This is the body of the sample post.")

# Selecting the status from the dropdown menu
time.sleep(2)  # Delay for 2 seconds
driver.find_element(By.ID, "id_status").send_keys(status)

# Entering the tags
time.sleep(2)  # Delay for 2 seconds
driver.find_element(By.ID, "id_tags").send_keys(tags)

# Submiting the form by clicking the "Save" button
time.sleep(2)  # Delay for 2 seconds
save_button = driver.find_element(By.XPATH, '//*[@id="post_form"]/div/div/input[1]')
save_button.click()


time.sleep(2)  # Delay for 2 seconds


# Find the logout btn and submit it
logout_button = driver.find_element(By.XPATH, '//*[@id="logout-form"]/button')
logout_button.click()


# Wait for the logout to complete and then open the posts list link
time.sleep(2)  
driver.get("http://127.0.0.1:8000/blog/")


# Wait for the page to load completely
driver.implicitly_wait(5)

# Find all the post titles on the page
post_titles = driver.find_elements(By.XPATH, "//h2/a")

# Loop through each post title
for post_title in post_titles:
    # Get the text of the post title
    title_text = post_title.text
    # Check if the title matches the random_title
    if random_title in title_text:

        time.sleep(2)  # Delay for 2 seconds

        # Click on the post link
        post_title.click()
        break  # Stop the loop after finding and clicking on the matching post link


# Optionally, wait for user input to keep the browser open
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
