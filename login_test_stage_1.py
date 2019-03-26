from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.fullscreen_window()


driver.get("http://newtours.demoaut.com/mercurysignon.php")
driver.find_element_by_name("userName").send_keys("testacademy@mailinator.com")
driver.find_element_by_name("password").send_keys("TEST1234")
driver.find_element_by_name("login").click()

driver.find_element_by_link_text("SIGN-OFF").click()


driver.close()
driver.quit()


