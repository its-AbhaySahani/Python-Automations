from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Ethical Considerations and Disclaimer
# This code is for demonstration purposes only. Automating flight bookings
# can violate website terms of service and potentially lead to unexpected
# consequences. Entering personal information into a script is also
# a security risk. It's strongly recommended to book flights manually
# through the travel website.

# User Input
print("**Disclaimer:** This script is for demonstration purposes only.")
user_confirmation = input("Do you still want to proceed? (y/n): ")

if user_confirmation.lower() != 'y':
    print("Exiting script...")
    exit()

# Replace with the actual path to your ChromeDriver
chrome_driver_path = "path/to/chromedriver"

# Set up WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open Go Indigo website
driver.get("https://www.goindigo.in/")

# Verify landing page
current_url = driver.current_url
page_title = driver.title

if current_url != "https://www.goindigo.in/" or not page_title:
    print("Error: Could not verify landing on Go Indigo website.")
    driver.quit()
    exit()

print(f"Current URL: {current_url}")
print(f"Page Title: {page_title}")

# Click Book option
book_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#_baptn-toggle-nav-menu"))
)
book_button.click()

# Click Flight option
flights_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-toggle='tooltip'][title='Flights']"))
)
flights_option.click()

# Click 1 Pax option (if applicable)
one_pax_option = driver.find_element(By.CSS_SELECTOR, "[aria-label='1 Adult']")
if one_pax_option.is_displayed():
    one_pax_option.click()

# Increase Adults to 2 and click Done
adult_count = driver.find_element(By.ID, "adultPax")
adult_count.clear()
adult_count.send_keys("2")

done_button = driver.find_element(By.CSS_SELECTOR, "#paxInformation .done")
done_button.click()

# Enter From and To locations
from_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "originStation1"))
)
from_field.send_keys("Hyderabad")

to_field = driver.find_element(By.ID, "destinationStation1")
to_field.send_keys("Delhi")

# Select Hyderabad and Delhi from dropdown menus
hyderabad_option_from = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@id='glsuggest_wrapper_originStation1']//div[text()='Hyderabad (HYD)']")
    )
)
hyderabad_option_from.click()

delhi_option_to = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@id='glsuggest_wrapper_destinationStation1']//div[text()='Delhi (DEL)']")
    )
)
delhi_option_to.click()

# Select one month from current date
travel_date_field = driver.find_element(By.ID, "departureDate1")
travel_date_field.click()

# Select the first available date
available_dates = travel_date_field.find_elements(By.XPATH, "//div[@class='day']")
available_dates[0].click()

# Click Search Flight Button
search_button = driver.find_element(By.ID, "search_btn")
search_button.click()

# Wait for search results to load
search_results = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".flight-card"))
)

# Click on the first recommendation
first_recommendation = search_results.find_elements(By.CSS_SELECTOR, ".flight-card")[0]
first_recommendation.click()

# Click Next
next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary.btn-lg"))
)
next_button.click()

# Enter passenger details
passenger_details_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".passenger-details"))
)

# Select Male for gender
gender_select = passenger_details_section.find_element(By.ID, "gender")
gender_select.click()
Select(gender_select).select_by_value("M")

# Fill First Name, Last Name, and DOB fields
first_name_field = passenger_details_section.find_element(By.ID, "firstName")
first_name_field.send_keys("John")  # Replace with actual first name

last_name_field = passenger_details_section.find_element(By.ID, "lastName")
last_name_field.send_keys("Doe")  # Replace with actual last name

dob_field = passenger_details_section.find_element(By.ID, "dob")
dob_field.send_keys("01-01-1990")  # Replace with actual date of birth

# **Important - User Interaction Required**
print("**Please wait for the passenger details page to load and manually enter the remaining details.**")

# Close the browser
driver.quit()