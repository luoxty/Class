from selenium import webdriver;
driver = webdriver.Chrome();
driver.get("https://www.baidu.com/")
driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click();
driver.switch_to.window(driver.window_handles[1]);
driver.find_element_by_link_text("清明假期将至，这份防护指南请查收！").click();
print(driver.current_window_handle);#打印当前窗口
print(driver.window_handles);#打印所有窗口
print(driver.window_handles[1])#打印第二个窗口
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_link_text("教育").click();

