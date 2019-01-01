import HTMLTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class WebTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://easythink.top')

    def test_open(self):
        self.assertEquals(self.driver.title, 'EasyThink', 'title error')

    def test_login(self):
        login_btn = self.driver.find_element_by_css_selector('#down > ul.nav.navbar-nav.navbar-right > li > a')
        login_btn.click()
        ac = ActionChains(self.driver)
        name = self.driver.find_element_by_css_selector('#username_email')
        pwd = self.driver.find_element_by_css_selector('#password')
        login = self.driver.find_element_by_css_selector('#submit')
        ac.send_keys_to_element(name, 'ppp').send_keys_to_element(pwd, 'qqq').click(login).perform()
        self.assertTrue('login' not in self.driver.current_url)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([WebTest("test_open"), WebTest("test_login")])

    with open('./res.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='blog test',
            verbosity=2
        )
        runner.run(suite)
