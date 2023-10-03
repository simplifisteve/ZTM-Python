from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=chrome_options)
# chrome_browser.maximize_window() 

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')

user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I am extra COOL!")

show_message_button.click()

chrome_browser.implicitly_wait(10)
# output_message = chrome_browser.find_element(By.ID, "display")

# user_button = chrome_browser.find_element(By.CSS_SELECTOR, "#get-input > .btn") # select element using css selector
# print(user_button)

chrome_browser.close()

# # Explicit Wait to check if output message is displayed
# def test_explicit(driver):
#     driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
#     revealed = driver.find_element(By.ID, "revealed")
#     wait = WebDriverWait(driver, timeout=2)

#     driver.find_element(By.ID, "reveal").click()
#     wait.until(lambda d : revealed.is_displayed())

#     revealed.send_keys("Displayed")
#     assert revealed.get_property("value") == "Displayed"