import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get("https://www.reddit.com/login/")
    username_field = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
    )
    username_field.send_keys("memmedovamil045@gmail.com")
    
    password_field = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
    )
    password_field.send_keys("A1m2i3q4o5")
    
    submit_buttons = [
        "button[type='submit']",   
        "button[data-click-id='login']", 
        "button[class*='m-full-width']",
    ]

    for selector in submit_buttons:
        try:
            login_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            login_button.click()
            break
        except:
            continue

def test_profile_customization():
    driver = webdriver.Chrome()
    login(driver)
    driver.get("https://www.reddit.com/settings/")
    
    try:
        profile_link = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/settings/profile']"))
        )
        profile_link.click()
        
        profile_pic_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        profile_pic_input.send_keys("/yeni/profil/fotografi/yolu.jpg")
        
        save_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='Save']"))
        )
        save_button.click()
        
        assert "Profile updated" in driver.page_source
    finally:
        driver.quit()
