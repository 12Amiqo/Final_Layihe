def login():
    import pytest
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get("https://www.reddit.com/login/")
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
    )
    username_field.send_keys("memmedovamil045@gmail.com")
    
    

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_authorization():
    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/login/")
    
    try:
        username_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )
        username_field.send_keys("kullanici_adiniz")
        
        password_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
        )
        password_field.send_keys("sifreniz")
        
        # Birkaç farklı submit butonunu kontrol ediyoruz
        submit_buttons = [
            "button[type='submit']",   # Genel buton
            "button[data-click-id='login']", # Özel data attribute butonu
            "button[class*='m-full-width']", # Özel class attribute
        ]

        for selector in submit_buttons:
            try:
                login_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                login_button.click()
                break
            except:
                continue
        
        # Giriş işleminin başarılı olup olmadığını kontrol et
        WebDriverWait(driver, 30).until(
            EC.title_contains("reddit")
        )
    finally:
        driver.quit()
