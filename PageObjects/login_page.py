import time

from selenium.webdriver.common.by import By


class Login:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//*[@type='submit']"
    invalid_text = "//p[text()='Invalid credentials']"
    #Add employee details
    button_addemp_xpath = "//a[contains(text(),'Add Employee')]"
    img_insert = "//input[@class='oxd-file-input']"
    textbox_1stname_xpath = "//*[@name='firstName']"
    textbox_midname_xpath = "//*[@name='middleName']"
    textbox_lastname_xpath = "//*[@name='lastName']"
    textbox_emp_idclr="//*[contains(text(),'Employee Id')]/../..//*[@class='oxd-input oxd-input--active']"
    button_save_xpath = "//button[@type='submit']"
    #personal data
    textbox_dob_xpath = "//*[contains(text(),'Date of Birth')]/../..//input[@placeholder='yyyy-mm-dd']"
    dropbox_nationtly_xpath = "//*[contains(text(),'Nationality')]/../..//*[@class='oxd-select-text--after']"
    dropbox_select_xpath = "//*[@class='oxd-select-option'][84]"
    select_sex = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label"
    dropbox_marrage_xpath = "//*[contains(text(),'Marital Status')]/../..//*[@class='oxd-select-wrapper']"
    dropbox_marr_select_xpath = "//*[contains(text(),'Single')]"
    personal_data_savebut = "//button[@type='submit']"
    #JOB details
    job_details_xpath = "//*[text()='Job']"
    #job_joind_date_click = "//*[contains(text(),'Joined Date')]/../..//*[@class='oxd-input oxd-input--active']"
    job_joind_date_enter = "//*[contains(text(),'Joined Date')]/../..//*[@placeholder='yyyy-mm-dd']"
    job_title_xpath = "//*[contains(text(),'Job Title')]/../..//*[@class='oxd-select-wrapper']"
    job_title_select_xpath = "//*[contains(text(),'Job Title')]/../..//*[contains(text(),'QA Engineer')]"
    job_subunit_xpath="//*[contains(text(),'Sub Unit')]/../..//*[@class='oxd-select-wrapper']"
    job_subunit_sele_xpath="//*[contains(text(),'Sub Unit')]/../..//*[contains(text(),'Development')]"
    emply_sts_xpath="//*[contains(text(),'Employment Status')]/../..//*[@class='oxd-select-wrapper']"
    emply_sts_sele_xpath="//*[contains(text(),'Employment Status')]/../..//*[contains(text(),'Full-Time Permanent')]"
    job_detail_save_but = "//button[@type='submit']"
    #creat details in add
    checkbox_addinfo_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    textbox_uname_xpath = "//*[text()='Username']/../..//*[@class='oxd-input oxd-input--active']"
    textbox_password_xpath = "//*[text()='Password']/../..//*[@type='password']"
    textbox_confpassword_xpath = "//*[text()='Confirm Password']/../..//*[@type='password']"
    ##employee edit
    emp_search_xpath = "//*[contains(text(),'Employee Name')]/../..//*[@placeholder='Type for hints...']"
    search_button_xpath = "//button[@type='submit']"
    sugg_click = "//*[contains(text(),'chinddu game')]"
    click_etid_btn = "//*[@class='oxd-icon bi-pencil-fill']"
    drivers_lis_no = "//*[contains(text(),'Driver')]/../..//*[@class='oxd-input oxd-input--active']"
    emp_save_xpath = "//*[@type='submit']"
    report_to_xpath = "//*[contains(text(),'Report-to')]"
    #delete emp details
    delete_icon_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def verify_login(self):
        var = self.driver.find_element(By.XPATH, self.invalid_text).text
        return var

    def add_emp_data(self,u_name,u_password):
        self.driver.find_element(By.XPATH, self.button_addemp_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.img_insert).send_keys("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\testData\\img files\\img1.png")
        self.driver.find_element(By.XPATH, self.textbox_1stname_xpath).send_keys('chinddu')
        self.driver.find_element(By.XPATH, self.textbox_midname_xpath).send_keys('game')
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys('S')
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_emp_idclr).clear()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.checkbox_addinfo_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_uname_xpath).send_keys(u_name)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(u_password)
        self.driver.find_element(By.XPATH, self.textbox_confpassword_xpath).send_keys(u_password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def personal_data(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.dropbox_nationtly_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.dropbox_select_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_dob_xpath).send_keys('2022-10-03')
        self.driver.find_element(By.XPATH, self.select_sex).click()
        self.driver.find_element(By.XPATH, self.dropbox_marrage_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dropbox_marr_select_xpath).click()
        self.driver.find_element(By.XPATH, self.personal_data_savebut).click()

    #JOB details
    def enter_job_details(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.job_details_xpath).click()
        time.sleep(5)
        #self.driver.find_element(By.XPATH, self.job_joind_date_click).click()
        self.driver.find_element(By.XPATH, self.job_joind_date_enter).send_keys('2022-10-03')
        self.driver.find_element(By.XPATH,self.job_title_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.job_title_select_xpath).click()
        self.driver.find_element(By.XPATH,self.job_subunit_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.job_subunit_sele_xpath).click()
        self.driver.find_element(By.XPATH,self.emply_sts_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.emply_sts_sele_xpath).click()
        self.driver.find_element(By.XPATH,self.job_detail_save_but).click()

    def emp_search(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.emp_search_xpath).send_keys("chinddu")
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.sugg_click).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def edit_emp(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.click_etid_btn).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.drivers_lis_no).send_keys("ADP15J156")
        #self.driver.find_element(By.XPATH,self.report_to_xpath).click()

        self.driver.find_element(By.XPATH,self.emp_save_xpath).click()

    def delete_user_data(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@type='button' and @class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()











