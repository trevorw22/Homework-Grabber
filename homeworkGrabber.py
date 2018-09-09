# A little script I created to scrape and print all of my Black Board practice homeworks to pdfs for later studying.
# Since I used some XPath elements, this script might not function properly if Black Board updates their website.
# This script will definitely help you study for some classes because it creates a practice homework study bank.

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import pyautogui

driver = webdriver.Chrome()

# Replace this URL with your schools blackboard link.
driver.get("https://uni.blackboard.com")

def page_is_loaded(driver):
	return driver.find_element_by_tag_name("body") != None

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("usernameGoesHere")
password.send_keys("passwordGoesHere")
driver.find_element_by_name("login").click()

# Not the real link to my course below, but it will look something like this.
# Make sure your link contains the course_id= parameter in it.
driver.get("https://blackboard.com/webapps/blackboard/content/launchAssessment.jsp?course_id=_123456_1&content_id=_123456_1&mode=view")

driver.find_element_by_name("top_Begin").click()
driver.find_element_by_xpath("//*[@id='containerdiv']/div[2]/a[2]").click()
driver.find_element_by_xpath("//*[@id='navpaging_top']/button[2]/img").click()
driver.find_element_by_xpath("//*[@id='dataCollectionContainer']/p[1]/input").click()

pyautogui.typewrite(['enter'], interval=1)

driver.find_element_by_xpath("//*[@id='containerdiv']/p[2]/a").click()

pyautogui.hotkey('ctrl', 'p')
pyautogui.typewrite(['enter'], interval=1)
pyautogui.typewrite(['enter'], interval=1)
pyautogui.typewrite(['enter'], interval=1)
pyautogui.hotkey('alt', 'tab')

driver.find_element_by_xpath("//*[@id='containerdiv']/p[2]/a").click()
