import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        driver_location = "/usr/local/bin/chromedriver"
        binary_location = "/usr/bin/google-chrome"
        options = webdriver.ChromeOptions()
        options.binary_location = binary_location
        self.driver = webdriver.Chrome(executable_path=driver_location, options=options)
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_example(self):
        print("Test Asserted False")
        assert False  # AssertionError FAILED

    def test_example_2(self):
        print("Test Asserted True")
        assert True

    def not_a_test(self):
        # will not run since function does not start with test
        print("this won't print")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
