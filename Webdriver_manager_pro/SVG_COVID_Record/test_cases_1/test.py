from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

driver = Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/search?q=covid+cases+in+india&rlz=1C1FKPE_enIN953IN953&oq=covid&aqs=chrome.3.69i57j0i433i512j0i131i433i512j0i433i512l2j0i131i433i512l2j69i60.5095j0j7&sourceid=chrome&ie=UTF-8")
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,1800);")


