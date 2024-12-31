from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def find_element_not_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def type(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text
    
    def get_attribute_href(self, locator):
        return self.find_element(locator).get_attribute("href")
    
    def get_attribute_name(self, locator):
        return self.find_element(locator).get_attribute("name")
    
    def get_attribute_value(self, locator):
        return self.find_element(locator).get_attribute("value")
    
    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()
    
    def is_not_displayed(self, locator):
        return self.find_element_not_visible(locator)
    
    def scroll_to_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(locator)).perform()

    def switch_to_alert(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            return alert
        except:
            raise Exception("Alert not found")

    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.switch_to_alert()
        alert.dismiss()

    def get_alert_text(self):
        alert = self.switch_to_alert()
        return alert.text

    def send_keys_to_alert_accept(self, text):
        alert = self.switch_to_alert()
        alert.send_keys(text)
        alert.accept() 

    def send_keys_to_alert_dismiss(self, text):
        alert = self.switch_to_alert()
        alert.send_keys(text)
        alert.dismiss() 

    def switch_to_frame(self, locator):
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def get_current_url(self) :
        return self.driver.current_url

    def navigate_url(self, url) :
        self.driver.get(url)

    def switch_to_window_by_index(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
