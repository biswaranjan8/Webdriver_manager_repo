from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

import time
driver = Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.google.com/search?q=covid+cases+in+india&rlz=1C1FKPE_enIN953IN953&oq=covid&aqs=chrome.3.69i57j0i433i512j0i131i433i512j0i433i512l2j0i131i433i512l2j69i60.5095j0j7&sourceid=chrome&ie=UTF-8")
driver.implicitly_wait(10)
covid_data = driver.find_elements_by_xpath("//*[local-name()='svg' and @class='uch-psvg']//*[name()='rect']")

time.sleep(2)
act = ActionChains(driver)

for i in covid_data:
    # We have visualise move to cursor
    act.move_to_element(i).perform()
    data = driver.find_element_by_xpath("//div[@class='ExnoTd']")
    print(data.text)


