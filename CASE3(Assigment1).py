import os
import subprocess
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.extensions.android.nativekey import AndroidKey
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

# Set the desired capabilities for the iPad Air device
desired_caps = {
    "platformName": "Android",
    "udid": "356110070756124",
    "platformVersion": "7.1.1",
    "automationName": "UiAutomator2",
    "browserName": "Chrome"
}
# Launch the Daraz website
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.get("https://www.daraz.pk/")
time.sleep(5)
user_action = TouchAction(driver)
user_action.tap(x=114, y=304).perform()
time.sleep(5)
user_action2 = TouchAction(driver)
user_action2.tap(x=170, y=179).perform()

time.sleep(2)


# Define the coordinates you want to enter

# coordinates = [(149, 948), (75, 940),(571, 1040),(149, 948),(478, 843),(504, 1040),(358, 948),(391, 1137),
#                (571, 1040),(607, 846),(429, 1038),(540, 848),(645, 950),(178, 823)]
#
# # Type "Samsung mobile"
# for coord in coordinates:
#     action = TouchAction(driver)
#     action.tap(x=coord[0], y=coord[1]).perform()
#     time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'text', '"Samsung mobile With Free Delivery"'])
driver.execute_script('mobile:performEditorAction', {'action': 'Search'})
time.sleep(5)
# Create a TouchAction object and perform the swipe gesture
action = TouchAction(driver)
action.press(x=178, y=1105).wait(200).move_to(x=628, y=243).release().perform()
time.sleep(5)
use = TouchAction(driver)
use.tap(x=142, y=898).perform()
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
action1 = TouchAction(driver)
action1.press(x=178, y=871).wait(200).move_to(x=333, y=473).release().perform()

user_ac2 = TouchAction(driver)
user_ac2.tap(x=513, y=1003).perform()
# add to cart
time.sleep(5)
user_ac3 = TouchAction(driver)
user_ac3.tap(x=609, y=1153).perform()
time.sleep(5)
user_ac4 = TouchAction(driver)
user_ac4.tap(x=356, y=1151).perform()
time.sleep(5)

time.sleep(1)
action2 = TouchAction(driver)
action2.press(x=176, y=900).wait(200).move_to(x=615, y=203).release().perform()
time.sleep(5)
user_ac4 = TouchAction(driver)
user_ac4.tap(x=218, y=203).perform()

time.sleep(5)
user_ac5 = TouchAction(driver)
user_ac5.tap(x=603, y=1164).perform()

time.sleep(5)
user_ac6 = TouchAction(driver)
user_ac6.tap(x=617, y=1124).perform()


# driver.get("https://www.daraz.pk/products/samsung-galaxy-a04-65-inch-display-4gb-ram-64gb-rom-i396464368-s1921801494.html?spm=a2a0e.searchlist.list.13.28e86f4cvbr37M&search=1")
# coordinates2 = [(591, 1139), (357, 1139)]
# user_action3 = TouchAction(driver)
# user_action3.tap(x=685, y=1141).perform()
# time.sleep(5)
# user_action4 = TouchAction(driver)
# user_action4.tap(x=553, y=1136).perform()
# time.sleep(5)
# user_action5 = TouchAction(driver)
# user_action5.tap(x=553, y=1136).perform()

# driver.get("https://www.daraz.pk/products/samsung-galaxy-a04-65-inch-display-4gb-ram-64gb-rom-i396464368-s1921801494.html?spm=a2a0e.searchlist.list.13.28e86f4cvbr37M&search=1")
# time.sleep(5)
# # user_action8 = TouchAction(driver)
# # user_action8.tap(x=630, y=289).perform()
# # time.sleep(5)
# # user_action6 = TouchAction(driver)
# # user_action6.tap(x=521, y=1133).perform()
# # user_action6 = TouchAction(driver)
# # user_action6.tap(x=521, y=1133).perform()
# #
# # user_action7 = TouchAction(driver)
# # user_action7.tap(x=108, y=451).perform()
# # time.sleep(5)
# coordinates = [(630, 289), (517, 1145), (517, 1145), (517, 1145), (108, 451)]
#
# # Type "Samsung mobile"
# for coord in coordinates:
#     action = TouchAction(driver)
#     action.tap(x=coord[0], y=coord[1]).perform()
#     time.sleep(5)
#
# # os.system('adb shell input text "ahsan.8840@iqra.edu.pk"')
# # # Type "ahsan.8840@iqra.edu.pk"
# # time.sleep(5)
# subprocess.run(['adb', 'shell', 'input', 'text', 'ahsan.8840@iqra.edu.pk'])
#
# driver.execute_script('mobile:performEditorAction', {'action': 'Search'})
# time.sleep(5)
# subprocess.run(['adb', 'shell', 'input', 'text', 'Ahsan@123'])
# time.sleep(5)
# driver.execute_script('mobile:performEditorAction', {'action': 'Search'})
# time.sleep(5)
#
# coordinates2 = [(161, 1155), (52, 1139), (54, 1141), (603, 1130), (280, 471), (241, 517), (358, 414), (358, 414),
#                 (329, 406), (329, 406), (546, 527)]
#
# # Type "Samsung mobile"
# for coord2 in coordinates2:
#     action = TouchAction(driver)
#     action.tap(x=coord2[0], y=coord2[1]).perform()
#     time.sleep(5)
#
# subprocess.run(['adb', 'shell', 'input', 'text', 'Ahsan'])
# user_action9= TouchAction(driver)
# user_action9.tap(x=544, y=632).perform()
# #
# # Send the key codes for the phone number to the device using adb shell input
# coordinates3 = [(509, 766),  (98, 620), (94, 724), (167, 1162), (98, 749)]
# #(345, 1141), (496, 672)
# # # Type "Samsung mobile"
# for coord3 in coordinates3:
#     action = TouchAction(driver)
#     action.tap(x=coord3[0], y=coord3[1]).perform()
#     time.sleep(5)
# # subprocess.run(['adb', 'shell', 'input', 'text', 'north karachi xyz'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_1'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_2'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_3'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_4'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_5'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_6'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_7'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_8'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_9'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_0'])
#
# touc = TouchAction(driver)
# touc.press(x=130, y=613).move_to(x=377, y=377).release().perform()
# time.sleep(5)
# coordinates4 = [(492, 429),  (71, 630), (69, 726), (100, 745), (178, 1162), (360, 1141), (471, 655)]
# #
# # # Type "Samsung mobile"
# for coord4 in coordinates4:
#     action = TouchAction(driver)
#     action.tap(x=coord4[0], y=coord4[1]).perform()
#     time.sleep(5)
# subprocess.run(['adb', 'shell', 'input', 'text', 'north karachi xyz'])

