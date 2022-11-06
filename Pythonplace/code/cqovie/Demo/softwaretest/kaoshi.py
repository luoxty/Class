#1
#from  selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.gmw.cn/')
# driver.find_element_by_id('searchText').send_keys('科技军事前沿')

# 2
# from  selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.find_element_by_name('wd').send_keys('国内咨询')

#3
from selenium.webdriver.common import by
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://www.people.com.cn/")
# driver.find_element_by_xpath('//*[@<img src="/img/2020peopleindex/img/t_logo1.png"]').click()



#4
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element(by=By.CLASS_NAME, value='s_ipt').send_keys('光明导读')



# 5
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.find_element_by_id('kw').send_keys('通过id定位')



