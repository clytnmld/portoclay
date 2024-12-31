from pageObjects.loginPage import LoginPage
from pageObjects.basePage import BasePage
import time

def test_socials(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)  # Class name is LoginPage; variable is login_page
    base_page = BasePage(driver)

    login_page.click_linkedin()
    driver.switch_to.window(driver.window_handles[-1])
    current_url = base_page.get_current_url()
    print(current_url)
    assert current_url == "https://www.linkedin.com/company/orangehrm"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    login_page.click_facebook()
    driver.switch_to.window(driver.window_handles[-1])
    current_url = base_page.get_current_url()
    print(current_url)
    assert current_url == "https://www.facebook.com/OrangeHRM/"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    login_page.click_twitter()
    driver.switch_to.window(driver.window_handles[-1])
    current_url = base_page.get_current_url()
    print(current_url)
    assert current_url == "https://x.com/orangehrm?lang=en&mx=2"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    login_page.click_youtube()
    driver.switch_to.window(driver.window_handles[-1])
    current_url = base_page.get_current_url()
    print(current_url)
    assert current_url == "https://www.youtube.com/c/OrangeHRMInc"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_loginValid(driver) :
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)  # Class name is LoginPage; variable is login_page
    base_page = BasePage(driver)
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

def test_loginInvalid(driver) :
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)  # Class name is LoginPage; variable is login_page
    base_page = BasePage(driver)
    login_page.enter_username('Admin1')
    login_page.enter_password('admin1231')
    login_page.click_login()
    invalid_alert = login_page.get_alertInvalid()
    assert invalid_alert == "Invalid credentials"

def test_forgotPassword(driver) :
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)  # Class name is LoginPage; variable is login_page
    base_page = BasePage(driver)
    login_page.click_forgotPassword()
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"

def test_ofcPage(driver) :
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)  # Class name is LoginPage; variable is login_page
    base_page = BasePage(driver)
    login_page.click_ofcLink()
    login_page.switch_to_window_by_index(1)
    current_url = base_page.get_current_url()
    print(current_url)
    assert current_url == "https://www.orangehrm.com/"
    driver.close()
    login_page.switch_to_window_by_index(0)
    current_url = base_page.get_current_url()
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
