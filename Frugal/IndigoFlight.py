import datetime
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndigoFlightBook:
    def __init__(self, driver, from_city, to_city, arrival_month, arrival_flight_date, return_month, return_flight_date):
        self.driver = driver
        self.from_city = from_city
        self.to_city = to_city
        self.arrival_month = arrival_month
        self.arrival_flight_date = arrival_flight_date
        self.return_month = return_month
        self.return_flight_date = return_flight_date
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.close_pop_up()

    def close_pop_up(self):
        wait = WebDriverWait(self.driver, 10) # Wait for 10 seconds
        try:
            # Wait for the pop-up's close button and click it
            close_ad = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='flight-close']")))
            close_ad.click()
            logging.info("Advertisement closed")
        except:
            print("No advertisement found.")
        time.sleep(5)
        # Step 2: Click on "Book" option
        book_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'headerv2__navbar-item') and contains(text(), 'Book')]")))
        book_dropdown.click()
        logging.info("Clicked on 'Book' button")
        time.sleep(5)

    def cookie_handle(self):
        cookie_close = self.driver.find_element(By.XPATH, "//a[@class='close-cookie accept-cookies__block--close']")
        cookie_close.click()
        time.sleep(2)

    def from_place(self):
        from_input = self.driver.find_element(By.XPATH, "//input[@class='input-text-field__input' and @placeholder='From']")
        from_input.send_keys(self.from_city)
        time.sleep(3)

    def to_place(self):
        to_input = self.driver.find_element(By.XPATH, "//input[@class='input-text-field__input' and @placeholder='To']")
        to_input.send_keys(self.to_city)
        time.sleep(3)

    def select_picked_date_month(self, month, date, booking_type):
        today = datetime.datetime.today()
        assert month >= today.month, "Given month should be greater than or equal to the current month"
        next_button = self.driver.find_element(By.XPATH, "//div[@class='react-datepicker']/button")
        if booking_type == 'arrival':
            for i in range(month - today.month):
                next_button.click()

        if booking_type == 'return':
            for i in range(self.return_month - self.arrival_month):
                next_button.click()

        selected_month = self.driver.find_element(By.XPATH, "(//div[@class='react-datepicker']//div[@class='react-datepicker__month-container'])")
        date_element = selected_month.find_element(By.XPATH, f'//div[text()="{date}"]')
        disabled = date_element.get_attribute("aria-disabled")
        assert disabled == 'false', "Date is in the past"
        date_element.click()
        time.sleep(3)

    def fetch_arrival_date(self):
        self.driver.find_element(By.XPATH, '//div[@id="travel-dates-container"]').click()
        time.sleep(3)
        booking_type = 'arrival'
        self.select_picked_date_month(self.arrival_month, self.arrival_flight_date, booking_type)

    def fetch_return_date(self):
        self.driver.find_element(By.XPATH, "//div[@class='custom-form-control input-text-field to-date']").click()
        time.sleep(3)
        booking_type = 'return'
        self.select_picked_date_month(self.return_month, self.return_flight_date, booking_type)

    def searched_flight_navigated_page(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Flights on these dates are not available.']")))
        if 'Flights on these dates are not available.' in element.text:
            print('Flights are not available for selected data')
        else:
            wait = WebDriverWait(self.driver, 10)
            results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='search-result-page__search-results__list']//div[@class='search-result-page__search-results__list__item   ']")))
            print(len(results))
            for result in results:
                flight_departure_time = result.find_element(By.XPATH, "//div[@class='flight-departure-time']/span")
                print(f'Flight Departure: {flight_departure_time.text}')
                flight_arrival_time = result.find_element(By.XPATH, "//div[@class='flight-arrival-time']/span")
                print(f'Flight Arrival: {flight_arrival_time.text}')
                flight_number = result.find_element(By.XPATH, "//div[@class='flight-Accordion-number']//span[@class='flight-number']")
                print(f'Flight Number: {flight_number.text}')
                flight_stops = result.find_element(By.XPATH, "//div[@class='flight-stops']")
                print(f'Flight Stops: {flight_stops.text}')
                flight_fare = result.find_element(By.XPATH, "//span[@class='selected-fare__price']")
                print(f'Flight fare: {flight_fare.text}')

    def click_search_flight_button(self):
        search_flight = self.driver.find_element(By.XPATH, "//button[@class='custom-button ']")
        search_flight.click()
        time.sleep(3)
        print('Button clicked')
        self.searched_flight_navigated_page()

from_city = input('Please enter from city ')
to_city = input('Please enter to city ')
arrival_month = int(input('Enter the valid month for which you want to book arrival flight: '))
arrival_flight_date = int(input('Enter the date for arrival flight: '))
return_month = int(input('Enter the valid month for which you want to book return flight: '))
return_flight_date = int(input('Enter the date for return flight: '))
url = 'https://www.goindigo.in/'
driver = webdriver.Chrome()
driver.get(url)
obj = IndigoFlightBook(driver, from_city, to_city, arrival_month, arrival_flight_date, return_month, return_flight_date)
obj.cookie_handle()
obj.from_place()
obj.to_place()
obj.fetch_arrival_date()
obj.fetch_return_date()
obj.click_search_flight_button()

driver.quit()