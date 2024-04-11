#https://www.cowin.gov.in
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

# Home page window
driver.get("https://www.cowin.gov.in/")
covin_window = driver.window_handles[0]
covin_window_url = driver.current_url
print("Covin HOME PAGE Window URL:", covin_window_url)

# FAQ Window - click on the "FAQ" link
driver.find_element(By.LINK_TEXT, "FAQ").click()
time.sleep(3)
faq_window = driver.window_handles[1]
driver.switch_to.window(faq_window)
faq_window_url = driver.current_url
print("FAQ Window URL:", faq_window_url)

# PARTNERS Window - click on the "PARTNERS" link
driver.find_element(By.LINK_TEXT, "PARTNERS").click()
time.sleep(3)
partner_window = driver.window_handles[2]
driver.switch_to.window(partner_window)
partner_window_url = driver.current_url
print("PARTNER Window URL:", partner_window_url)

# Fetch the window handles (IDs) of the opened windows
window_handles = driver.window_handles

# Display the window handles (IDs) on the console
print("Window Handles (IDs) of the opened windows:")
for handle in window_handles:
    print(handle)

# To close Partner Window
driver.close()

# To close FAQ Window
driver.switch_to.window(faq_window)
driver.close()

# Switch back to Home page Window
driver.switch_to.window(covin_window)

# Quit the WebDriver
driver.quit()
