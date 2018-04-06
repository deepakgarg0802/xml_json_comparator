# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import jsoncompare

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver

        driver.get("https://www.browserling.com/tools/xml-to-json")
        driver.find_element_by_id("xml-to-json-text").click()
        driver.find_element_by_id("xml-to-json-text").clear()
        xml_content = open("./scratch_xml.xml").read();
        driver.find_element_by_id("xml-to-json-text").send_keys(xml_content)

        driver.find_element_by_id("xml-to-json-submit").click()
        driver.find_element_by_id("xml-to-json-text").click()

        json_output_from_net= driver.find_element_by_id("xml-to-json-text").get_attribute("value")


        #--------- Replace the attribute changes-----------
        json_output_from_net=json_output_from_net.replace("_","")
        json_output_from_net = json_output_from_net.replace("xaxis", "x-axis")
        json_output_from_net = json_output_from_net.replace("yaxis", "y-axis")

        print(json_output_from_net)

        jsoncompare.myf(json_output_from_net,"./scratch.json")

        print("############ Finished #############")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
