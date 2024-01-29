from multiprocessing import Value
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOnSurus_Sport(unittest.TestCase):
    def setUp(self):
        self.sitetest = "https://surus-shop.ru/"
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

    def initialize():
        return TestOnSurus_Sport
    
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
        login = element.text
        if login == "Личный кабинет":
            self.to_file("Test_1_passed")
        else:
            self.to_file("Test_1_failed")

#тест2 поиск по каталогу
    def test2(self):
        self.to_file("Test_2_start")
        self.driver.get(self.sitetest)  
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="title-search"]/form/input'))).clear()    #очистка поля
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="title-search"]/form/input'))).send_keys("Шорты")    #заполнение поля

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-dropdown"]/ul/li/ul/li[2]/a/span[2]/span[1]/b')))
        
        poisk = element.text
        if poisk == "Шорты":
            self.to_file("Test_2_passed")
        else:
            self.to_file("Test_2_failed")


#тест3 добавление товара в корзину
    def test3(self):
        self.to_file("Test_2_start")
        self.driver.get(self.sitetest)  
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74451"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74451_buy_link74730"]'))).click()

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_cart_block"]/span/span[2]')))
        
        poisk = element.text
        if poisk == "1 позиция на 330 руб.":
            self.to_file("Test_3_passed")
        else:
            self.to_file("Test_3_failed")



if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestOnSurus_Sport('test1'))
    suite.addTest(TestOnSurus_Sport('test2'))
    suite.addTest(TestOnSurus_Sport('test3'))
    #suite.addTest(TestOnSurus_Sport('test4'))
    #suite.addTest(TestOnSurus_Sport('test5'))
    #suite.addTest(TestOnSurus_Sport('test6'))
    #suite.addTest(TestOnSurus_Sport('test7'))
    #suite.addTest(TestOnSurus_Sport('test8'))
    #suite.addTest(TestOnSurus_Sport('test9'))
    #suite.addTest(TestOnSurus_Sport('test10'))

    unittest.TextTestRunner().run(suite)