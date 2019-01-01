from selenium import webdriver
import unittest


class WebTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        # self.driver.get('http://easythink.top')

    def test_es(self):
        # self.driver.find_element_by_css_selector('body > div.navbar.navbar-default > div > div.navbar-header > a')
        # self.assertEquals(self.driver.title, 'EasyThink2', 'title error')
        self.help()

    def help(self):
        print('hhh')

    def tearDown(self):
        print('teardown')


if __name__ == '__main__':
    unittest.main()