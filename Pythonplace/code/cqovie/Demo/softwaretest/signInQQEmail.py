from selenium import webdriver;
from time import sleep;
driver = webdriver.Chrome();
driver.get('https://mail.qq.com');
driver.find_element_by_id("wither_plogin").click();
sleep(2)
username = 3228244175
driver.find_element_by_id("u").send_keys(3228244175)
