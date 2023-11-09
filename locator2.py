from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.gmail.com")

"""
element = driver.find_element("id", "element_id")"""
email = driver.find_element("id", "email")

email.send_keys("ezhilarasiece1992@gmail.com")

password = driver.find_element("id", "pass")
password.send_keys("EEEEllll15")

log = driver.find_element("xpath", '//*[@id="u_0_5_2K"]')
log.click()


