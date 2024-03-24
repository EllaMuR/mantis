# noinspection PyInterpreter
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.mantis_project import MantisProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):#, username, password
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Opera":
            self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
#       self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.mantis_project = MantisProjectHelper(self)
        self.base_url = config['web']['baseUrl']


        # self.password = password
        # self.username = username


    def open_homepage(self):
        wd = self.wd
        wd.get(self.base_url)
        # if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//input[@value='Login']")) > 0):
        #     wd.get("http://localhost/addressbook/")
    #
    #
    #
    # def go_to_homepage(self):
    #     wd = self.wd
    #     if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))>0):
    #         wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
