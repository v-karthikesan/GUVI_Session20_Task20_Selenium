#https://labour.gov.in/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

driver = webdriver.Chrome(options=opt)

# Launching labour.gov.in Webpage
driver.get("https://labour.gov.in")
first_window = driver.current_window_handle

# Downloading Monthly Progress Report from Documents menu
try:
    # Find and click on the "Documents" menu
    doc_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Documents")))
    action = ActionChains(driver)
    action.move_to_element(doc_search)
    action.perform()

    # Find and click on the "Monthly Progress Report" link
    progress_report_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Monthly Progress Report")))
    progress_report_link.click()
    progress_report_link1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Download(221.53 KB)")))
    progress_report_link1.click()
    time.sleep(3)

    # Switch to the alert and accept it
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

except Exception as e:
    print("An error occurred while downloading the Monthly Progress Report:", e)

finally:
    # Switch back to the first window
    time.sleep(3)
    driver.switch_to.window(first_window)


    # Find the "Media" menu
    media_search=driver.find_element(By.LINK_TEXT, "Media")
    action.move_to_element(media_search)
    action.perform()
    time.sleep(5)
    # Print message if "Photo Gallery" not available in Media menu
    print("Photo Gallery not available in Media menu")
    # Quit the WebDriver
    driver.quit()
