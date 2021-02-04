import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class fail_test(unittest.TestCase):
    def setUp(self):
        PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_search_in_python_org(self):
        false_answer = 'Je ne me souviens plus de rien'
        self.driver.get("https://grandpy-jilvo.herokuapp.com/")
        self.driver.find_element_by_id("user_input").send_keys("fdpghfwjfdg")
        element = self.driver.find_element_by_id("api_google")
        element.click()
        time.sleep(3)
        element_test = self.driver.find_element_by_id("test_bubble").text
        print(element_test)
        time.sleep(3)
        self.driver.quit()
        assert false_answer == element_test
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

class success_test(unittest.TestCase):
    def setUp(self):
        PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_search_in_python_org(self):
        true_answer = 'Assis toi, je vais tout te raconter'
        self.driver.get("https://grandpy-jilvo.herokuapp.com/")
        self.driver.find_element_by_id("user_input").send_keys("Où est le mont Fugi ?")
        element = self.driver.find_element_by_id("api_google")
        element.click()
        time.sleep(3)
        element_test = self.driver.find_element_by_id("test_bubble").text
        print(element_test)
        time.sleep(3)
        self.driver.quit()
        assert true_answer == element_test
    def tearDown(self):
        time.sleep(3)
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