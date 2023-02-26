import subprocess
import time

from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.extensions.android.nativekey import AndroidKey
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

# Set the desired capabilities for the iPad Air device
desired_caps = {
    "platformName": "Android",
    "udid": "356110070756124",
    "platformVersion": "7.1.1",
    "automationName": "UiAutomator2",
    "browserName": "Chrome"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.get("https://www.daraz.pk/")
time.sleep(5)
user_action = TouchAction(driver)
user_action.tap(x=114, y=304).perform()
time.sleep(5)
user_action2 = TouchAction(driver)
user_action2.tap(x=170, y=179).perform()

time.sleep(2)
subprocess.run(['adb', 'shell', 'input', 'text', 'Mobiles'])
time.sleep(5)
driver.execute_script('mobile:performEditorAction', {'action': 'Search'})
time.sleep(5)
user_action3 = TouchAction(driver)
user_action3.tap(x=175, y=863).perform()
time.sleep(10)

# add to cart with friend with you prompt

user_actio7 = TouchAction(driver)
user_actio7.tap(x=630, y=1147).perform()
time.sleep(10)

# user_actio8 = TouchAction(driver)
# user_actio8.tap(x=151, y=1151).perform()
# time.sleep(10)


user_actio9 = TouchAction(driver)
user_actio9.tap(x=377, y=1141).perform()
time.sleep(10)
# login Page successful registration
coordinates = [(557, 1139), (557, 1139), (100, 452)]

for coord in coordinates:
    action = TouchAction(driver)
    action.tap(x=coord[0], y=coord[1]).perform()
    time.sleep(5)
subprocess.run(['adb', 'shell', 'input', 'text', 'ahsan.8840@iqra.edu.pk'])

driver.execute_script('mobile:performEditorAction', {'action': 'Search'})
time.sleep(5)
subprocess.run(['adb', 'shell', 'input', 'text', 'Ahsan@123'])
time.sleep(5)
driver.execute_script('mobile:performEditorAction', {'action': 'Search'})
time.sleep(5)
# go back to chose new product
driver.back()
driver.back()
driver.back()
driver.back()
driver.back()
time.sleep(5)
user_act = TouchAction(driver)
user_act.tap(x=557, y=1132).perform()
time.sleep(5)
# user_act = TouchAction(driver)
# user_act.tap(x=557, y=1132).perform()
# add to cart
time.sleep(5)
user_ac2 = TouchAction(driver)
user_ac2.tap(x=609, y=1153).perform()
time.sleep(5)
user_ac2 = TouchAction(driver)
user_ac2.tap(x=356, y=1151).perform()
time.sleep(5)
user_ac2 = TouchAction(driver)
user_ac2.tap(x=356, y=1151).perform()
#
# us = TouchAction(driver)
# us.tap(x=364, y=1149).perform()
# time.sleep(10)

# upon = TouchAction(driver)
# upon.tap(x=624, y=289).perform()
# time.sleep(10)
#
driver.back()
time.sleep(5)

us = TouchAction(driver)
us.tap(x=486, y=793).perform()

# add to cart
time.sleep(5)
user_ac3 = TouchAction(driver)
user_ac3.tap(x=609, y=1153).perform()
time.sleep(5)
user_ac4 = TouchAction(driver)
user_ac4.tap(x=356, y=1151).perform()
time.sleep(5)
user_ac4 = TouchAction(driver)
user_ac4.tap(x=356, y=1151).perform()
driver.back()
time.sleep(5)
TouchAction(driver)   .press(x=657, y=567)   .move_to(x=663, y=576)   .release()   .perform()
click_onckeck = TouchAction(driver)
click_onckeck.tap(x=620, y=285).perform()
time.sleep(5)

driver.get("https://cart-m.daraz.pk/cart?spm=a2a0e.searchlist.site-header.dcart.28615ea48dyxns&thirdPartLoginCb=")
time.sleep(10)
TouchAction(driver)   .press(x=657, y=567)   .move_to(x=663, y=576)   .release()   .perform()
time.sleep(10)
# for product in products:
#     price_element = product.find_element(By.XPATH, ".//div[@class='c3gUW0']//span[@class='c13VH6']")
#     if "Free delivery" in product.text and int(price_element.text.replace(",", "")) < 50000:
#         add_to_cart_button = product.find_element(By.XPATH, ".//button[@class='c3gUW0']")
#         add_to_cart_button.click()
click_onckeck = TouchAction(driver)
click_onckeck.tap(x=657, y=567).perform()
time.sleep(5)
time.sleep(5)
TouchAction(driver)   .press(x=657, y=567)   .move_to(x=663, y=576)   .release()   .perform()
time.sleep(10)
click_onckeck = TouchAction(driver)
click_onckeck.tap(x=657, y=567).perform()
time.sleep(5)
time.sleep(5)
TouchAction(driver)   .press(x=657, y=567)   .move_to(x=663, y=576)   .release()   .perform()
time.sleep(10)
click_onckeck = TouchAction(driver)
click_onckeck.tap(x=657, y=567).perform()
time.sleep(5)