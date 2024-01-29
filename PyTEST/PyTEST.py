﻿from multiprocessing import Value
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOnSurus_Sport(unittest.TestCase):
    def setUp(self):
        self.sitetest = "https://surus-shop.ru/"
        #self.sitetest2 = ""
        self.file_path = r"C:\Users\Kazimir\Documents\testlog\test.log"
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def to_file(self, text):
        try:
            with open(self.file_path, 'a') as file:
                file.write(text + '\n')
            print(f"Text appended to {self.file_path}")
        except FileNotFoundError:
            with open(self.file_path, 'w') as file:
                file.write(text + '\n')
            print(f"File {self.file_path} created, and text appended")

#тест1 вход по логину и паролю
    def test1(self):
        self.to_file("Test_1_start")
        self.driver.get(self.sitetest)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_personal_menu"]'))).click()    #нажать кнопку   
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[1]'))).clear()    #очистка поля
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[2]'))).clear()
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[1]'))).send_keys("barboss8208@gmail.com")    #заполнение поля
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[2]'))).send_keys("test1234")
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/button'))).click()    #нажать кнопку   

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_personal_menu"]/a')))
        login=element.text
        if login == "Личный кабинет":
            self.to_file("Test_1_passed")
        else:
            self.to_file("Test_1_failed")

#тест1 вход по логину и паролю








if __name__ == "__main__":
    suite = unittest.TestSuite()

   
    suite.addTest(TestOnSurus_Sport('test1'))
    #suite.addTest(TestOnSurus_Sport('test2'))
    #suite.addTest(TestOnSurus_Sport('test3'))
    #suite.addTest(TestOnSurus_Sport('test4'))
    #suite.addTest(TestOnSurus_Sport('test5'))
    #suite.addTest(TestOnSurus_Sport('test6'))
    #suite.addTest(TestOnSurus_Sport('test7'))
    #suite.addTest(TestOnSurus_Sport('test8'))
    #suite.addTest(TestOnSurus_Sport('test9'))
    #suite.addTest(TestOnSurus_Sport('test10'))

    unittest.TextTestRunner().run(suite)