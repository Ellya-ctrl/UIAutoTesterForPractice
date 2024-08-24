from selenium.webdriver.support.wait import WebDriverWait
import time
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import selenium
import allure

# блок селекторов для формы

firstNameSelector = (By.ID, 'firstName')
lastNameSelector = (By.ID, 'lastName')
emailSelector = (By.ID, 'userEmail')
dateSelector = (By.ID, "dateOfBirthInput")
sendButtonSelector = (By.ID, 'submit')
maleGenderSelector = (By.CSS_SELECTOR, 'input[value="Male"]')
femaleGenderSelector = (By.CSS_SELECTOR, 'input[value="Female"]')
otherGenderSelector = (By.CSS_SELECTOR, 'input[value="Other"]')
mobileSelector = (By.CSS_SELECTOR, '#userNumber')
monthSelector = (By.CSS_SELECTOR, '.react-datepicker__month-select')
yearSelector = (By.CSS_SELECTOR, '.react-datepicker__year-select')
daySelector = lambda x: (By.XPATH,
                         f'//div[contains(@class, "react-datepicker__day--{x:03d}") and not(@class="react-datepicker__day--outside-month")]')
subjectsSelector = (By.XPATH, '//*[@id="subjectsInput"]')
subjects_valueSelector = (By.XPATH, "//*[contains(text(), 'English')]")
hobbySportsSelector = (By.XPATH, '//*[@id="hobbies-checkbox-1"]')
hobbyReadingSelector = (By.XPATH, '//*[@id="hobbies-checkbox-2"]')
hobbyMusicSelector = (By.XPATH, '//*[@id="hobbies-checkbox-3"]')
pictureSelector = (By.XPATH, '//*[@id="uploadPicture"]')
currentAddressSelector = (By.XPATH, '//*[@id="currentAddress"]')
stateSelector = (By.XPATH, '//*[@id="state"]')
state_valueSelector = (By.XPATH, "//*[contains(text(), 'NCR')]")
citySelector = (By.XPATH, '//*[@id="city"]')
city_valueSelector = (By.XPATH, "//*[contains(text(), 'Delhi')]")
thanksTableTitle = (By.XPATH, '//*[@id="example-modal-sizes-title-lg"]')
firstAndLastNameTable = (By.XPATH, "//*/table/tbody/tr[1]/td[2]")
emailTable = (By.XPATH, "//*/table/tbody/tr[2]/td[2]")
genderTable = (By.XPATH, "//*/table/tbody/tr[3]/td[2]")
mobileTable = (By.XPATH, "//*/table/tbody/tr[4]/td[2]")
dateTable = (By.XPATH, "//*/table/tbody/tr[5]/td[2]")
subjectsTable = (By.XPATH, "//*/table/tbody/tr[6]/td[2]")
hobbyTable = (By.XPATH, "//*/table/tbody/tr[7]/td[2]")
imageTable = (By.XPATH, "//*/table/tbody/tr[8]/td[2]")
addressTable = (By.XPATH, "//*/table/tbody/tr[9]/td[2]")
stateAndCityTable = (By.XPATH, "//*/table/tbody/tr[10]/td[2]")

#Сам класс страницы
class RegestrationFormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, url):
        with allure.step('Открывает - "Regestration form page"'):
            self.open_url(url)

    @property
    def thanksTitle(self):
        return self.find(thanksTableTitle)

    def thanksTitleIsDisplayed(self):
        with allure.step('Проверяет отбражён ли - "thanksTitle"  '):
            return self.thanksTitle.is_displayed()

    @property
    def SendButton(self):
        return self.find(sendButtonSelector)

    def clickSendButton(self):
        with allure.step('Кнопка отправки данных нажата'):
            self.SendButton.click()

    @property
    def firstName(self):
        return self.find(firstNameSelector)

    def sendFirstName(self, word):
        with allure.step('Вводит -"First Name"'):
            self.firstName.clear()
            self.firstName.send_keys(word)

    @property
    def lastName(self):
        return self.find(lastNameSelector)

    def sendLastName(self, word):
        with allure.step('Вводит -"Last Name"'):
            self.lastName.clear()
            self.lastName.send_keys(word)

    @property
    def email(self):
        return self.find(emailSelector)

    def sendEmail(self, emaiL):
        with allure.step('Вводит -"Email"'):
            self.email.clear()
            self.email.send_keys(emaiL)

    def sendGender(self, gendeR):
        with allure.step('Вводит -"Gender"'):
            genderOBJ = self.browser.find_elements(By.XPATH, "//input[@type='radio']")
            if gendeR == 'Male':
                genderOBJ[0].send_keys(selenium.webdriver.common.keys.Keys.SPACE)
            elif gendeR == 'Female':
                genderOBJ[1].send_keys(selenium.webdriver.common.keys.Keys.SPACE)
            else:
                genderOBJ[2].send_keys(selenium.webdriver.common.keys.Keys.SPACE)

    @property
    def mobile(self):
        return self.find(mobileSelector)

    def sendMobile(self, mobilE):
        with allure.step('Вводит -"Mobile"'):
            self.mobile.clear()
            self.mobile.send_keys(mobilE)

    @property
    def dateOfBirth(self):
        return self.find(dateSelector)

    def openCalendar(self):
        with allure.step('Открывает календарь'):
            self.dateOfBirth.click()

    def sendMonth(self, month):
        with allure.step('Вводит -"Month"'):
            Month = self.find(monthSelector)
            select = Select(Month)
            select.select_by_value(month)

    def sendYear(self, year):
        with allure.step('Вводит -"Year"'):
            Year = self.find(yearSelector)
            select = Select(Year)
            select.select_by_value(year)

    def sendDay(self, day):
        with allure.step('Вводит -"Day"'):
            Day = self.find(daySelector(day))
            Day.click()

    @property
    def subjects(self):
        return self.find(subjectsSelector)

    def sendSubjects(self, subjecT):
        with allure.step('Вводит -"Subject"'):
            self.subjects.clear()
            self.subjects.send_keys(subjecT)
            time.sleep(2)
            subject = self.browser.find_element(*subjects_valueSelector)
            subject.click()

    def sendHobby(self, hobbY):
        with allure.step('Вводит -"Hobby'):
            hobbyOBJ = self.browser.find_elements(By.XPATH, "//input[@type='checkbox']")
            if hobbY == 'Sports':
                hobbyOBJ[0].send_keys(selenium.webdriver.common.keys.Keys.SPACE)
            elif hobbY == 'Reading':
                hobbyOBJ[1].send_keys(selenium.webdriver.common.keys.Keys.SPACE)
            else:
                hobbyOBJ[2].send_keys(selenium.webdriver.common.keys.Keys.SPACE)

    @property
    def picture(self):
        return self.find(pictureSelector)

    def sendPicture(self, path):
        with allure.step('Вводит -"Picture"'):
            self.picture.clear()
            self.picture.send_keys(path)

    @property
    def currentAddress(self):
        return self.find(currentAddressSelector)

    def sendAddress(self, address):
        with allure.step('Вводит -"Address"'):
            self.currentAddress.clear()
            self.currentAddress.send_keys(address)

    @property
    def state(self):
        return self.find(stateSelector)

    def sendState(self):
        with allure.step('Вводит -"State'):
            self.state.click()
            state_value = self.find(state_valueSelector)
            state_value.click()

    @property
    def city(self):
        return self.find(citySelector)

    def sendCity(self):
        with allure.step('Вводит -"City'):
            self.city.click()
            city_value = self.find(city_valueSelector)
            city_value.click()

    def checkAllResults(self, firstAndLastname, email, gender, mobile, date, subject, hobby, image, address, stateAndCity):
        with allure.step('Начало проверки всех полученных данных'):

            # блок тестирования
            if self.thanksTitleIsDisplayed():
                if (self.check(firstAndLastNameTable, firstAndLastname) == True and self.check(emailTable, email) == True and self.check(genderTable, gender) == True and
                    self.check(mobileTable, mobile) == True and self.check(dateTable, date) == True and self.check(subjectsTable, subject) == True and
                    self.check(hobbyTable, hobby) == True and self.check(imageTable, image) == True and self.check(addressTable, address) == True and
                    self.check(stateAndCityTable, stateAndCity) == True
                ):
                    with allure.step('Программа завершена успешно, тест пройден'):
                        return True
                else:
                    with allure.step('Программа сломана, тест не завершён'):
                        return False
            else:
                with allure.step('Данные введены неверно'):
                    return False