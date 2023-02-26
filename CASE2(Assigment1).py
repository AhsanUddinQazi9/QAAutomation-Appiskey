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

driver.get("https://cart-m.daraz.pk/cart?spm=a2a0e.searchlist.site-header.dcart.28615ea48dyxns&thirdPartLoginCb=")
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
start_x = 612
start_y = 509
end_x = 269
end_y = 52

# Create a TouchAction object and perform the swipe gesture
action = TouchAction(driver)
action.press(x=start_x, y=start_y).wait(200).move_to(x=end_x, y=end_y).release().perform()
time.sleep(10)
user_act = TouchAction(driver)
user_act.tap(x=629, y=515).perform()
time.sleep(5)
action = TouchAction(driver)
action.press(x=start_x, y=start_y).wait(200).move_to(x=end_x, y=end_y).release().perform()
time.sleep(10)
user_act = TouchAction(driver)
user_act.tap(x=629, y=515).perform()
time.sleep(5)
ction = TouchAction(driver)
action.press(x=start_x, y=start_y).wait(200).move_to(x=end_x, y=end_y).release().perform()
time.sleep(10)
user_act = TouchAction(driver)
user_act.tap(x=629, y=515).perform()
driver.quit()