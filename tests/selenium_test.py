import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class fail_test(unittest.TestCase):
    def setUp(self):
        PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_search_in_python_org(self):
        log_dic = {'Succés'}
        self.driver.get("https://grandpy-jilvo.herokuapp.com/")
        self.driver.find_element_by_id("user_input").send_keys("Paris")
        element = self.driver.find_element_by_id("api_google")
        element.click()
        data = self.driver.get_log('browser')
        print(data)
        time.sleep(1)
        self.driver.quit()
        assert log_dic == data
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
        
        # self.assertIn("GrandPy-Bot", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
# Fail = fail_test()
# Fail.test_search_in_python_org()