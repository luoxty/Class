# from selenium import webdriver;
# from time import sleep;
# driver = webdriver.Chrome();
# driver.maximize_window();
# driver.get("https://www.baidu.com/")
# news1=driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]');
# driver.execute_script("arguments[0].removeAttribute('target')",news1);
# news1.click()
# news2=driver.find_element_by_link_text("上海疫情特点？难点？突破点？");
# driver.execute_script("arguments[0].removeAttribute('target')",news2);
# news2.click()

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id("kw").send_keys("通过id进行定位")

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_name("kw").send_keys("通过name进行定位")