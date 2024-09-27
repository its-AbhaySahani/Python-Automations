import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Logger;

public class IndigoFlightBook {
    private WebDriver driver;
    private String fromCity;
    private String toCity;
    private int arrivalMonth;
    private int arrivalFlightDate;
    private int returnMonth;
    private int returnFlightDate;
    private static final Logger logger = Logger.getLogger(IndigoFlightBook.class.getName());

    public IndigoFlightBook(WebDriver driver, String fromCity, String toCity, int arrivalMonth, int arrivalFlightDate, int returnMonth, int returnFlightDate) {
        this.driver = driver;
        this.fromCity = fromCity;
        this.toCity = toCity;
        this.arrivalMonth = arrivalMonth;
        this.arrivalFlightDate = arrivalFlightDate;
        this.returnMonth = returnMonth;
        this.returnFlightDate = returnFlightDate;
        this.driver.manage().window().maximize();
        this.driver.manage().timeouts().implicitlyWait(5, java.util.concurrent.TimeUnit.SECONDS);
        this.closePopUp();
    }

    public void closePopUp() {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        try {
            // Wait for the pop-up's close button and click it
            WebElement closeAd = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//span[@class='flight-close']")));
            closeAd.click();
            logger.info("Advertisement closed");
        } catch (Exception e) {
            System.out.println("No advertisement found.");
        }
        try {
            Thread.sleep(5000); // Wait for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // Step 2: Click on "Book" option
        try {
            WebElement bookDropdown = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//div[contains(@class,'headerv2__navbar-item') and contains(text(), 'Book')]")));
            bookDropdown.click();
            logger.info("Clicked on 'Book' button");
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            Thread.sleep(5000); // Wait for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void cookieHandle() {
        WebElement cookieClose = driver.findElement(By.xpath("//a[@class='close-cookie accept-cookies__block--close']"));
        cookieClose.click();
        try {
            Thread.sleep(2000); // Wait for 2 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void fromPlace() {
        WebElement fromInput = driver.findElement(By.xpath("//input[@class='input-text-field__input' and @placeholder='From']"));
        fromInput.sendKeys(fromCity);
        try {
            Thread.sleep(3000); // Wait for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void toPlace() {
        WebElement toInput = driver.findElement(By.xpath("//input[@class='input-text-field__input' and @placeholder='To']"));
        toInput.sendKeys(toCity);
        try {
            Thread.sleep(3000); // Wait for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void selectPickedDateMonth(int month, int date, String bookingType) {
        LocalDate today = LocalDate.now();
        if (month < today.getMonthValue()) {
            throw new IllegalArgumentException("Given month should be greater than or equal to the current month");
        }
        WebElement nextButton = driver.findElement(By.xpath("//div[@class='react-datepicker']/button"));
        if (bookingType.equals("arrival")) {
            for (int i = 0; i < month - today.getMonthValue(); i++) {
                nextButton.click();
            }
        } else if (bookingType.equals("return")) {
            for (int i = 0; i < returnMonth - arrivalMonth; i++) {
                nextButton.click();
            }
        }

        WebElement selectedMonth = driver.findElement(By.xpath("(//div[@class='react-datepicker']//div[@class='react-datepicker__month-container'])"));
        WebElement dateElement = selectedMonth.findElement(By.xpath("//div[text()='" + date + "']"));
        String disabled = dateElement.getAttribute("aria-disabled");
        if (disabled.equals("true")) {
            throw new IllegalArgumentException("Date is in the past");
        }
        dateElement.click();
        try {
            Thread.sleep(3000); // Wait for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void fetchArrivalDate() {
        driver.findElement(By.xpath("//div[@id='travel-dates-container']")).click();
        try {
            Thread.sleep(3000); // Wait for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        selectPickedDateMonth(arrivalMonth, arrivalFlightDate, "arrival");
    }

    public void fetchReturnDate() {
        driver.findElement(By.xpath("//div[@class='custom-form-control input-text-field to-date']")).click();
        try {
            Thread.sleep(3000); // Wait for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        selectPickedDateMonth(returnMonth, returnFlightDate, "return");
    }

    public void searchedFlightNavigatedPage() {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement element = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//p[text()='Flights on these dates are not available.']")));
        if (element.getText().contains("Flights on these dates are not available.")) {
            System.out.println("Flights are not available for selected data");
        } else {
            List<WebElement> results = wait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(By.xpath("//div[@class='search-result-page__search-results__list']//div[@class='search-result-page__search-results__list__item   ']")));
            System.out.println(results.size());
            for (WebElement result : results) {
                WebElement flightDepartureTime = result.findElement(By.xpath("//div[@class='flight-departure-time']/span"));
                System.out.println("Flight Departure: " + flightDepartureTime.getText());
                WebElement flightArrivalTime = result.findElement(By.xpath("//div[@class='flight-arrival-time']/span"));
                System.out.println("Flight Arrival: " + flightArrivalTime.getText());
                WebElement flightNumber = result.findElement(By.xpath("//div[@class='flight-Accordion-number']//span[@class='flight-number']"));
                System.out.println("Flight Number: " + flightNumber.getText());
                WebElement flightStops = result.findElement(By.xpath("//div[@class='flight-stops']"));
                System.out.println("Flight Stops: " + flightStops.getText());
                WebElement flightFare = result.findElement(By.xpath("//span[@class='selected-fare__price']"));
                System.out.println("Flight fare: " + flightFare.getText());
            }
        }
    }

    public void clickSearchFlightButton() {
        WebElement searchFlight = driver.findElement(By.xpath("//button[@class='custom-button ']"));
        searchFlight.click();
        try {
            Thread.sleep(3000); // Wait for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Button clicked");
        searchedFlightNavigatedPage();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter from city: ");
        String fromCity = scanner.nextLine();
        System.out.print("Please enter to city: ");
        String toCity = scanner.nextLine();
        System.out.print("Enter the valid month for which you want to book arrival flight: ");
        int arrivalMonth = scanner.nextInt();
        System.out.print("Enter the date for arrival flight: ");
        int arrivalFlightDate = scanner.nextInt();
        System.out.print("Enter the valid month for which you want to book return flight: ");
        int returnMonth = scanner.nextInt();
        System.out.print("Enter the date for return flight: ");
        int returnFlightDate = scanner.nextInt();
        scanner.close();

        String url = "https://www.goindigo.in/";
        WebDriver driver = new ChromeDriver();
        driver.get(url);

        IndigoFlightBook obj = new IndigoFlightBook(driver, fromCity, toCity, arrivalMonth, arrivalFlightDate, returnMonth, returnFlightDate);
        obj.cookieHandle();
        obj.fromPlace();
        obj.toPlace();
        obj.fetchArrivalDate();
        obj.fetchReturnDate();
        obj.clickSearchFlightButton();

        driver.quit();
    }
}