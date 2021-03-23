from selenium import webdriver

chrome_driver_path = "C:/Users/Vishal sepaia/Desktop/Git/webdriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.python.org/"

driver.get(URL)

element_time = driver.find_elements_by_css_selector(".event-widget time")
element_event = driver.find_elements_by_css_selector(".event-widget .menu a")

event = {}
for n in range(len(element_time)):
    event[n] = {
        "time": element_time[n].text,
        "event": element_event[n].text,
    }

print(event)
driver.close() # close tab
#driver.quit() # close entire browser