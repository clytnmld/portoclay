from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.forgot_password = (By.CSS_SELECTOR, "oxd-text.oxd-text--p.orangehrm-login-forgot-header")
        self.ofc_link = (By.CSS_SELECTOR, "a[href='http://www.orangehrm.com']")
        self.linkedin_link = (By.XPATH, "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']")
        self.facebook_link = (By.XPATH, "//a[@href='https://www.facebook.com/OrangeHRM/']")
        self.twitter_link = (By.XPATH, "//a[@href='https://twitter.com/orangehrm?lang=en']")
        self.youtube_link = (By.XPATH, "//a[@href='https://www.youtube.com/c/OrangeHRMInc']")
        self.forgot_password = (By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
        self.alert_invalid = (By.CSS_SELECTOR, "div[role='alert']")

    def enter_username(self, username):
        self.type(self.username_input, username)

    def enter_password(self, password):
        self.type(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def click_forgotPassword(self) :
        self.click(self.forgot_password)

    def click_ofcLink(self) :
        self.click(self.ofc_link)
    
    def click_linkedin(self):
        self.click(self.linkedin_link)
    
    def click_facebook(self):
        self.click(self.facebook_link)

    def click_twitter(self):
        self.click(self.twitter_link)

    def click_youtube(self):
        self.click(self.youtube_link)

    def click_forgotPassword(self):
        self.click(self.forgot_password)

    def get_alertInvalid(self):
        return self.get_text(self.alert_invalid)
    
    def click_forgotPassword(self):
        self.click(self.forgot_password)
