from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/Vishal sepaia/Desktop/Git/webdriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#URL = "https://en.wikipedia.org/wiki/Main_Page"
URL = "http://secure-retreat-92358.herokuapp.com/"

driver.get(URL)
#
# count = driver.find_element_by_css_selector("#articlecount a")
# print(count.text)
# #count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# #all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# #search_button = driver.find_element_by_id("searchButton")
# #search_button.click()


fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

fname.send_keys("Vishal")
lname.send_keys("Sepaia")
email.send_keys("vishal@gmail.com")
email.send_keys(Keys.ENTER)

#driver.close()