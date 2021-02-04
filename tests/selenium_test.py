from selenium import webdriver
import time

def test_search_in_python_org():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://grandpy-jilvo.herokuapp.com/")
    driver.find_element_by_id("user_input").send_keys("fdhhhhvshdsdhsdhjhvs")
    element = driver.find_element_by_id("api_google")
    element.click()
    data = driver.get_log('browser')
    print(data)
    time.sleep(10)
    driver.close()

    # self.assertIn("GrandPy-Bot", driver.title)
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
test_search_in_python_org()