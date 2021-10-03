from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import time
driver = Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element_by_name('q').send_keys("vivekanada")
time.sleep(2)
data = driver.find_elements_by_xpath("//*[@class='wM6W7d WggQGd']")

for i in data:
    print(i.text)


