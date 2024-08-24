class BasePage:
    # Инициализация браузера
    def __init__(self, browser):
        self.browser = browser

    # Открывает веб страницу по данному адресу
    def open_url(self, url):
        return self.browser.get(url)

    # Находит элемент на странице
    def find(self, args):
        return self.browser.find_element(*args)

    # Находит эелемент для проверки и проверяет по значению
    def check(self, selector, valueCheck):
        checkElement = self.find(selector)
        return checkElement.text == valueCheck
