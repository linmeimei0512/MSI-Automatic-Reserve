import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import cv2

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('detach', True)  # disable auto quit
prefs = {
    'credentials_enable_service': False,
    'profile.password_mamnger_enabled': False
}
chrome_options.add_experimental_option('prefs', prefs)

platform = sys.platform
if platform == 'linux':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                    options=chrome_options)
else:
    import os
    from subprocess import CREATE_NO_WINDOW

    chrome_install = ChromeDriverManager().install()
    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, 'chromedriver.exe')
    chrome_service = ChromeService(chromedriver_path)
    chrome_service.creation_flags = CREATE_NO_WINDOW
    driver = webdriver.Chrome(service=chrome_service,
                              options=chrome_options)

driver.get('https://rdraid5.msi.com.tw/DQA/Code/NewLabCenter/NewLab_ReserveHomePage.aspx?index=1&Labs=Reliability')
# driver.maximize_window()

# Login
login_btn = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_linkLog"]')
login_btn.click()

account_edit = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_pcLogin_LoginView1_Login1_UserName_I"]')
account_edit.send_keys('frankhmlo')
password_edit = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_pcLogin_LoginView1_Login1_Password_I"]')
password_edit.send_keys('Frank1122')
login_btn = driver.find_element(By.XPATH, value='//*[@id="ctl00_pcLogin_LoginView1_Login1_LoginButton_CD"]/span')
login_btn.click()

# Device
print('XXXXXX')
device_btn = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_DataList1"]/span[15]/li/div')
device_btn.click()

reserve_btn = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_ReserveDetailed_Modal_LBtn_reserve"]')
reserve_btn.click()


index = 0
for i in range(0, 100):
    captcha_image = driver.find_element(By.XPATH, value='//*[@id="captcha"]/canvas[1]')
    x, y = captcha_image.location['x'], captcha_image.location['y']
    width, height = captcha_image.size['width'], captcha_image.size['height']\

    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)

    captcha_image = cv2.imread(screenshot_path)[y:y+height, x:x+width]
    cv2.imwrite('./captcha/{}.png'.format(str(index + i).zfill(3)), captcha_image)

    create_btn = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_BtnReal_JustNew"]')
    create_btn.click()
    driver.switch_to.alert.accept()
