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

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_personal_menu"]'))).click()     
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[1]'))).clear()    
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[2]'))).clear()
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[1]'))).send_keys("barboss8208@gmail.com")   
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/div[1]/fieldset/input[2]'))).send_keys("test1234")
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/form/button'))).click()    

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_personal_menu"]/a')))
        login = element.text
        assert login == "Личный кабинет", "Тест 1 не пройден"
        self.to_file("Test_1_passed")

#тест2 поиск по каталогу
    def test2(self):
        self.to_file("Test_2_start")
        self.driver.get(self.sitetest)  
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="title-search"]/form/input'))).clear()    #очистка поля
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="title-search"]/form/input'))).send_keys("Шорты")    #заполнение поля

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-dropdown"]/ul/li/ul/li[2]/a/span[2]/span[1]/b')))
        
        poisk = element.text
        assert poisk == "Шорты", "Тест 2 не пройден"
        self.to_file("Test_2_passed")


#тест3 добавление товара в корзину
    def test3(self):
        self.to_file("Test_3_start")
        self.driver.get(self.sitetest)  
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74451"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74451_buy_link74730"]'))).click()

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_cart_block"]/span/span[2]')))
        tovar = element.text
        assert tovar == "1 позиция на 330 руб.", "Тест 3 не пройден"
        self.to_file("Test_3_passed")

#тест4 удаление товара из корзины
    def test4(self):
        self.to_file("Test_4_start")
        self.driver.get(self.sitetest)  
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74451"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74451_buy_link74730"]'))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/div[2]/div/div[3]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basket_items"]/div[2]/button'))).click()
        

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="empty_basket"]/div[2]/div[2]')))
        tovardel = element.text
        assert tovardel == "Ваша корзина пуста", "Тест 4 не пройден"
        self.to_file("Test_4_passed")

#тест5 сравнить товары
    def test5(self):
        self.to_file("Test_5_start")
        self.driver.get(self.sitetest)  
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74451"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74451_compare_link74730"]'))).click()
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74452"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74452_compare_link74735"]'))).click()
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_compare_count"]'))).click()

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_compare_count"]/span')))
        tovarvs = element.text
        assert tovarvs == "(2)", "Тест 5 не пройден"
        self.to_file("Test_5_passed")

#тест6 добавление товара в избранное
    def test6(self):
        self.to_file("Test_6_start")
        self.driver.get(self.sitetest) 

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74451"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74451_add_liked_compare_74730"]/div[1]/a'))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_favorite_count"]/a'))).click()

        time.sleep(4)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_favorite_count"]/a/span')))
        tovarlike = element.text
        assert tovarlike == "(1)", "Тест 6 не пройден"
        self.to_file("Test_6_passed")
            
#тест7 фильтрация списка товаров
    def test7(self):
        self.to_file("Test_7_start")
        self.driver.get(self.sitetest)
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="catalog-filter"]/div[1]/form[1]/div[3]/div[2]/div[1]/label[11]'))).click()

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modef"]/span')))
        tovarf = element.text
        assert tovarf == "6", "Тест 7 не пройден"
        self.to_file("Test_7_passed")

#тест8 сортировка списка товаров
    def test8(self):
        self.to_file("Test_8_start")
        self.driver.get(self.sitetest)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/section[1]/div[2]/article[1]/div[1]/div[1]/div[2]/div[1]/label[1]/div[1]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/section[1]/div[2]/article[1]/div[1]/div[1]/div[2]/div[1]/label[1]/div[1]/div[2]/ul/li[2]'))).click()

        time.sleep(2)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/section[1]/div[2]/article[1]/div[1]/div[1]/div[2]/div[1]/label[1]/div[1]/div[1]/div[1]')))
        tovarsort = element.text
        assert tovarsort == "Цене, сначала дорогие", "Тест 8 не пройден"
        self.to_file("Test_8_passed")

#тест9 расчет стоимости по количеству товара
    def test9(self):
        self.to_file("Test_9_start")
        self.driver.get(self.sitetest) 
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/nav/div/div/ul/li[1]'))).click()  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_3966226736_74451"]/div/div[2]/a'))).click() 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bx_117848907_74451_buy_link74730"]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/header/div[2]/div/div[3]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basket_items"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button'))).click()

        time.sleep(5)

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basket_items"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]')))
        tovar = element.text
        assert tovar == "660 руб.", "Тест 9 не пройден"
        self.to_file("Test_9_passed")

#тест10 переключение карусели баннеров
    def test10(self):
        self.to_file("Test_10_start")
        self.driver.get(self.sitetest)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/section[1]/div[1]/div[1]/div[3]/div[3]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/section[1]/div[1]/div[1]/div[3]/div[1]'))).click()
        
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/section[1]/div[1]/div[1]/div[3]/div[1]'))).get_attribute("class")
        assert element == "owl-dot active", "Тест 10 не пройден"
        self.to_file("Test_10_passed")


if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestOnSurus_Sport('test1'))
    suite.addTest(TestOnSurus_Sport('test2'))
    suite.addTest(TestOnSurus_Sport('test3'))
    suite.addTest(TestOnSurus_Sport('test4'))
    suite.addTest(TestOnSurus_Sport('test5'))
    suite.addTest(TestOnSurus_Sport('test6'))
    suite.addTest(TestOnSurus_Sport('test7'))
    suite.addTest(TestOnSurus_Sport('test8'))
    suite.addTest(TestOnSurus_Sport('test9'))
    suite.addTest(TestOnSurus_Sport('test10'))

    unittest.TextTestRunner().run(suite)