from pages.regestration_form import RegestrationFormPage
import pytest
import allure

#Набор значений для теста

firstName = "Bob"
lastName = "Nicholson"
email = "Nicholson@gmail.com"
gender = "Male"
mobile = "7943233123"
day = 13
monthNumber = "1"
month = "February"
year = "1974"
subject = "Eng"
subjectName = "English"
hobby = "Reading"
picture = r"C:\Users\User\PycharmProjects\UIAutoTesterForPractice\picture\Image.png"
pictureName = "Image.png"
currentAddress = 'NCR, Delhi, Baker-Street House-number 40'
state = "NCR"
city = "Delhi"


#Далее единственный тест проверяющий сразу всё, в allure есть множество его подпунктов
@pytest.mark.RegestrationForm
@allure.feature('Regestration form')
@allure.story('Regestration form')
def test_regestration_form_page(browser):
    regestrationFormPage = RegestrationFormPage(browser)
    regestrationFormPage.open('https://demoqa.com/automation-practice-form')
    #Старт ввода всех данных

    regestrationFormPage.sendFirstName(firstName)
    regestrationFormPage.sendLastName(lastName)
    regestrationFormPage.sendEmail(email)
    regestrationFormPage.sendGender(gender)
    regestrationFormPage.sendMobile(mobile)
    regestrationFormPage.openCalendar()
    regestrationFormPage.sendMonth(monthNumber)
    regestrationFormPage.sendYear(year)
    regestrationFormPage.sendDay(day)
    regestrationFormPage.sendSubjects(subject)
    regestrationFormPage.sendHobby(hobby)
    regestrationFormPage.sendPicture(picture)
    regestrationFormPage.sendAddress(currentAddress)
    regestrationFormPage.sendState()
    regestrationFormPage.sendCity()

    #Конец ввода данных и их отправка
    regestrationFormPage.clickSendButton()

    #Проверка полученных значний с введёнными на сайт
    assert regestrationFormPage.checkAllResults(firstName + " " + lastName, email, gender, mobile,
                                                str(day) + " " + month + "," + year,
                                                subjectName, hobby, pictureName, currentAddress, state + " " + city)
#Команды для старта:
#pytest -v -s --alluredir results
#allure serve results