from multiprocessing import Value
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOnlineSchool(unittest.TestCase):
    def setUp(self):
        self.sitetest = "https://ru.onlinemschool.com/"
        self.sitetest2 = "https://onlinemschool.com/"
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

    def test1(self):
        self.to_file("Test_1_start")
        self.driver.get(self.sitetest)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[1]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_kilotonne"]'))).send_keys(1)
        element = self.wait.until(EC.visibility_of_element_located((By.ID, 'oms_tonne')))
        value = int(element.get_attribute('value'))
        if value == 1000:
            self.to_file("Test_1_passed")
        else:
            self.to_file("Test_1_failed")
            
#Find X percentage of number Y.
    def test2(self):
        self.to_file("Test 2 start")
        self.driver.get(self.sitetest)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[4]/img'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c1"]'))).send_keys(10)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c2"]'))).send_keys(10)
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@onclick="percent1(\'oms_c\')"]'))).click()
        result_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="res_main_t"]/center/div')))
        result_text = result_element.text
        last_digit = result_text[-1]
        if last_digit == "1":
            self.to_file("Test 2 passed")
        else:
            self.to_file("Test 2 failed")
            
 #standart calc           
    def test3(self):
        self.to_file("Test 3 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[3]/td[2]/input'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[6]/td[3]/input'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[3]/td[2]/input'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[6]/td[4]/input'))).click()
        element=self.wait.until(EC.visibility_of_element_located((By.ID, 'oms_calc_res')))
        value = element.text
        if value =="16":
            self.to_file("Test 3 passed")
        else:
            self.to_file("Test 3 failed")
            
#search test
    def test4(self):
        self.to_file("Test 4 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[1]/div/div[1]/div/div/div'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gsc-i-id1"]'))).send_keys("Минор и алгебраическое дополнение матрицы.")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="___gcse_0"]/div/form/table/tbody/tr/td[2]/button'))).click()
        time.sleep(1)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="___gcse_1"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/a/b')))
        value=element.text
        if value =="Минор и алгебраическое дополнение матрицы":
            self.to_file("Test 4 passed")
        else:
            self.to_file("Test 4 failed")
            
#Column division      
    def test5(self):
        self.to_file("Test 5 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[2]/img'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[5]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c1"]'))).send_keys("6")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c2"]'))).send_keys("2")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_nabor"]'))).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="res_main_t"]/center/p[1]')))
        result_text = element.text
        last_digit = result_text[-1]
        if last_digit == "3":
            self.to_file("Test 5 passed")
        else:
            self.to_file("Test 5 failed")
            
#Unit converter. Degree Celsius
    def test6(self):
        self.to_file("Test 6 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[1]/img'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[8]'))).click()
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_close_1"]/table/tbody/tr[1]/td[1]/a'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_this_temp"]'))).send_keys("10")
        element = self.wait.until(EC.visibility_of_element_located((By.ID, 'oms_farengeyt')))
        value = element.text
        if value == "50":
            self.to_file("Test 6 passed")
        else:
            self.to_file("Test 6 failed")
        
        
#Cube area
    def test7(self):
        self.to_file("Test 7 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[18]/img'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c1"]'))).send_keys("1.4")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frtabl"]/p/input'))).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="res"]/div[2]')))
        text = element.text
        last_digit = text[-5:]
        if last_digit == "11.76":
         self.to_file("Test 7 passed")
        else:
         self.to_file("Test 7 failed")

#Downloading a file
    def test8(self):
        self.to_file("Test 8 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[5]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Скачать таблицу умножения")]'))).click()
        time.sleep(5)
        
        try:
           content_after_download = self.driver.page_source
           self.assertTrue(content_after_download)
           self.to_file("Test 8 passed")
        except:
           self.to_file("Test 8 failed")
#Graph of a function, download pictures 
    def test9(self):
        self.to_file("Test 9 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[6]/img'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frtabl"]/div/p[2]/input'))).click()
        element = self.driver.find_element(By.XPATH, '//span[@class="icon-oms-save"]')
        self.driver.execute_script("arguments[0].click();", element)

        time.sleep(5)
        
        try:
           content_after_download = self.driver.page_source
           self.assertTrue(content_after_download)
           self.to_file("Test 9 passed")
        except:
           self.to_file("Test 9 failed")
           
#change launge
    def test10(self):
        self.to_file("Test 10 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[1]/div/div[2]/div'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[1]/div/div[2]/ul/li[2]/a'))).click()
        self.wait.until(EC.url_to_be(self.sitetest2))
        self.driver.get(self.sitetest2)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/h1')))
        value = element.text
        print(value)
        if value == "Studying of mathematics onliney":
           self.to_file("Test 10 passed")
        else:
            self.to_file("Test 10 failed")
        
            



        
        

        


    
        

if __name__ == "__main__":
    suite = unittest.TestSuite()

   
    suite.addTest(TestOnlineSchool('test1'))
    suite.addTest(TestOnlineSchool('test2'))
    suite.addTest(TestOnlineSchool('test3'))
    suite.addTest(TestOnlineSchool('test4'))
    suite.addTest(TestOnlineSchool('test5'))
    suite.addTest(TestOnlineSchool('test6'))
    suite.addTest(TestOnlineSchool('test7'))
    suite.addTest(TestOnlineSchool('test8'))
    suite.addTest(TestOnlineSchool('test9'))
    suite.addTest(TestOnlineSchool('test10'))

    unittest.TextTestRunner().run(suite)