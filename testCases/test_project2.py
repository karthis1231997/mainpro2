from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utilities.readProperties import Readconfig
from utilities.custom_logger import LogGen
from PageObjects.login_page import Login
from utilities.var_wronguser import Verify
import time

class Test_orange():
    baseurl = Readconfig.getorangeurl()
    username = Readconfig.getuserid()
    password = Readconfig.getpassword()

    username_1 = Readconfig.getuserid_1()
    password_1 = Readconfig.getpassword_1()

    logger = LogGen.loggen()  # creating logging variable.


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("***Web page open***")
        login_page_obj = Login(self.driver)
        time.sleep(3)
        login_page_obj.set_username(self.username)
        login_page_obj.set_password(self.password)
        time.sleep(3)
        login_page_obj.click_login()
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\screenshots\\image1.png")
        self.logger.info("***Login success***")
        self.driver.close()

    def test_login_wrong(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login_page_obj = Login(self.driver)
        self.logger.info("***Web page open***")
        time.sleep(3)
        login_page_obj.set_username(self.username_1)
        login_page_obj.set_password(self.password_1)
        time.sleep(3)
        login_page_obj.click_login()
        data = login_page_obj.verify_login()
        data1 = data
        ver_user = Verify(self.driver)
        ver_user.ver_wrong_user(data1)
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\screenshots\\image2.png")
        self.driver.close()

    def test_sute_three(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login_page_obj = Login(self.driver)
        self.logger.info("***Web page open***")
        time.sleep(3)
        login_page_obj.set_username(self.username)
        login_page_obj.set_password(self.password)
        time.sleep(3)
        login_page_obj.click_login()
        self.logger.info("***login success***")
        username_c = Readconfig.Nusername()
        password_c = Readconfig.Npassword()
        login_page_obj.add_emp_data(username_c,password_c)
        login_page_obj.personal_data()
        login_page_obj.enter_job_details()
        self.logger.info("***job details added***")
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\screenshots\\image3.png")

    def test_login_edit(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login_page_obj = Login(self.driver)
        self.logger.info("***Web page open***")
        time.sleep(3)
        login_page_obj.set_username(self.username)
        login_page_obj.set_password(self.password)
        time.sleep(3)
        login_page_obj.click_login()
        login_page_obj.emp_search()
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\screenshots\\image4.png")
        login_page_obj.edit_emp()
        time.sleep(2)
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\screenshots\\image5.png")
        self.driver.close()

    def test_login_delete(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login_page_obj = Login(self.driver)
        self.logger.info("***Web page open***")
        time.sleep(3)
        login_page_obj.set_username(self.username)
        login_page_obj.set_password(self.password)
        time.sleep(3)
        login_page_obj.click_login()
        login_page_obj.emp_search()
        login_page_obj.delete_user_data()
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\screenshots\\image6.png")









