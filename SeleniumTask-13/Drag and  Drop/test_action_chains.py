import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_droppable():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    driver.get("https://jqueryui.com/droppable/")
    driver.maximize_window()

# SWITCH TO IFRAME
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

# FIND ELEMENT
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID,"droppable")

# DRAG AND DROP
    actions = ActionChains(driver)
    actions.drag_and_drop(source,target).perform()
    time.sleep(2)

    assert "Dropped!" in target.text
    driver.quit()



# ------------------------- NEGATIVE TEST CASE --------------------------
def test_droppable_negative(driver):
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))


    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(source,50, 40).perform()
    time.sleep(2)
    assert "Dropped!" not in target.text
