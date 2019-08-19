from django.test.testcases import LiveServerTestCase
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LiveServerIndexTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    def test_index_01(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertTemplateUsed('sample/index.html')
        self.assertEquals('Form Sample', self.selenium.title)

    def test_index_02(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        message_elem = self.selenium.find_element_by_css_selector('form textarea[name="message"]')
        message_elem.send_keys("Test Message")
        submit_elem = self.selenium.find_element_by_css_selector('form input[type="submit"]')
        submit_elem.click()
        WebDriverWait(self.selenium, 15).until(EC.visibility_of_all_elements_located)
        
        # assert Submit Success
        # self.assertEquals('Form Sample', self.selenium.title)

        # assert Submit 403 Error(CSRF Token Error)
        self.assertTrue('403' in self.selenium.title)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()