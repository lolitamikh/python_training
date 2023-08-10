# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_new_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("petrova")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("ivanova")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("anna")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("anya")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("spb")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("33")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("8800")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("500")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("123")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("anya@mail.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("spb")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("33")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("blabla")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
