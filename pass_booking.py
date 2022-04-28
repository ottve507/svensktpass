from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


import sys
import time
import traceback
from datetime import datetime


class PassBooking:

    #Constructor
    def __init__(self, early_time, late_time, emailaddr, telnumb, location_of_chrome_driver, start_page, number_of_people, personarray):
        self.early_time = early_time
        self.late_time = late_time
        self.emailaddr = emailaddr
        self.telnumb = telnumb
        self.location_driver = location_of_chrome_driver
        self.start_page = start_page
        self.number_of_people = number_of_people
        self.personarray = personarray
    
    #Function to check if an element exists
    def check_exists_by_xpath(self, driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    
    
    #Final confirmation page - confirming booking
    def confirm_booking(self,driver,datetime_object):
        delay = 15
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'Customer1')))
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/input")
        
        #Saves first screenshot
        driver.save_screenshot("booking_time.png")
        
        #Confirming time
        elem.click()
        time.sleep(120)
        
        #Saves second screenshot
        driver.save_screenshot("completed.png")
        driver.close()
        sys.exit()
        
        
    #Adding contact information
    def contact_info(self,driver, datetime_object):
        delay = 15
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'EmailAddress')))
     
        #Start filling out information to contact us.
        email = driver.find_element_by_xpath("//*[@id='EmailAddress']")
        email.send_keys(self.emailaddr)
        email_two = driver.find_element_by_xpath("//*[@id='ConfirmEmailAddress']")
        email_two.send_keys(self.emailaddr)
        phone = driver.find_element_by_xpath("//*[@id='PhoneNumber']")
        phone.send_keys(self.telnumb)
        phone_two = driver.find_element_by_xpath("//*[@id='ConfirmPhoneNumber']")
        phone_two.send_keys(self.telnumb)
        
        elem = driver.find_element_by_xpath("//*[@id='SelectedContacts_0__IsSelected']")
        elem.click()
        elem = driver.find_element_by_xpath("//*[@id='SelectedContacts_2__IsSelected']")
        elem.click()
        
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[2]/input")
        elem.click()
        
        self.confirm_booking(driver, datetime_object)

        
    
    #Accept info
    def accept_and_next(self,driver, datetime_object):
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/input")
        elem.click()
        self.contact_info(driver, datetime_object)
    
    
    #Accept that we want to order passport
    def enter_names(self, driver, datetime_object):
        delay = 15
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'Customers_0__BookingFieldValues_0__Value')))
        
        #Check in box that we want passport and id for first person
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div[5]/div/label[1]")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div[5]/div/label[2]")
        elem.click()
        
        if len(self.personarray)>0:
            for i in range(1, len(self.personarray)+1):
                elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div["+ str(i*5+2) +"]/div/span/input")
                elem.send_keys(self.personarray[i-1]['personnummer'])
                
                elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div["+ str(i*5+3) +"]/div/span/input")
                elem.send_keys(self.personarray[i-1]['firstname'])
                
                elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div["+ str(i*5+4) +"]/div/span/input")
                elem.send_keys(self.personarray[i-1]['lastname'])
                
                driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div["+ str(i*5+5) +"]/div/label[1]").click()
                driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div["+ str(i*5+5) +"]/div/label[2]").click()
             
      
        
        #Click continue
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[2]/input")
        elem.click()
        time.sleep(3)
        self.accept_and_next(driver, datetime_object)    
    
    #Find and select time
    def identify_dates(self,driver):
        
        found_time = False

        while found_time==False:        
            try:
                delay = 15
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'sectionName')))
                elems = driver.find_elements_by_css_selector(".pointer.timecell.text-center")
                print(len(elems))
                for x in elems:
                    datetime_object = datetime.strptime(x.get_attribute('data-fromdatetime'), '%Y-%m-%d %H:%M:%S')
                    print(datetime_object)
                 
                    if datetime_object < self.late_time and datetime_object > self.early_time:
                        x.click()
                        elem = driver.find_element_by_xpath("//*[@id='booking-next']")
                        elem.click()
                        
                        time.sleep(5)
                        #Check if we were able to go to next page
                        if self.check_exists_by_xpath(driver, "/html/body/div[2]/div/div/div/form/div[1]/div[5]/div/label[1]/input[1]"):
                            found_time = True
                            self.enter_names(driver, datetime_object)
                            
            except Exception:
                traceback.print_exc()
            
            
            time.sleep(25)
            driver.refresh()
    
    
    # Go to search times
    def search_times(self,driver):
        try:
            delay = 15
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'SearchTimeHour')))
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form[1]/div/div[6]/div/input[2]")
            elem.click()
            self.identify_dates(driver)
        except Exception:
            traceback.print_exc()
            driver.close()


    # Another accept page to click through
    def accept_boende(self,driver):
        try:
            delay = 15
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ServiceCategoryCustomers_0__ServiceCategoryId')))
            for i in range(1,self.number_of_people+1):
                elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div[" + str(i) + "]/div/label[1]")
                elem.click()
                            

            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[2]/input")
            elem.click()
            self.search_times(driver)
        except Exception:
            traceback.print_exc()
            driver.close()

    
    # Wait for a long time to see if new
    def approve_and_next(self,driver):
        try:
            delay = 700
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'AcceptInformationStorage')))
            elem = driver.find_element_by_xpath("//*[@id='AcceptInformationStorage']")
            elem.click()
            
            #Select how many people
            select = Select(driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[1]/div[3]/div/select"))
            select.select_by_value(str(self.number_of_people))
            
            
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[2]/input")
            elem.click()
            self.accept_boende(driver)
        except Exception:
            traceback.print_exc()
            driver.close()

    
    
    # logging in with bank id
    def log_in_with_bank_id(self, driver):
        
        try:
            delay = 15
            #Waiting for Mobile bank id button
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'a_wpki2')))
            #Clicking on mobile bank id
            elem = driver.find_element_by_xpath("/html/body/div/main/section/div/div[3]/nav/ul/li[2]/a")
            elem.click()
            
            self.approve_and_next(driver)
        except Exception:
            traceback.print_exc()
            driver.close()
    
    
    #Go to webpage
    def go_to_police(self):
    
        #The driver is set up
        driver = webdriver.Chrome(self.location_driver)

        driver.get(self.start_page)
        try:
            delay = 15
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ServiceGroupId')))
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div[1]/div/form/div[2]/input")
            elem.click()
            self.log_in_with_bank_id(driver)
        except Exception:
            traceback.print_exc()
            driver.close()
    