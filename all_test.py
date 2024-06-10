import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

# Sprint 5 Testleri
def test_authorization(driver):
    driver.get("https://www.reddit.com/login/")
    # Giriş elementlerini bulma
    username = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")
    # Kullanıcı adı ve şifre girme
    username.send_keys("memmedovamil045@gmail.com")
    password.send_keys("A1m2i3q4o5")
    password.send_keys(Keys.RETURN)
    # Başarılı girişi kontrol etme
    assert "reddit" in driver.title

def test_post_reactions(driver):
    driver.get("https://www.reddit.com/")
    # Bir gönderiye tıklama
    first_post = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Post")))
    first_post.click()
    # Beğenme, beğenmeme, gönderme ve kaydetme işlemleri
    upvote_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".voteButton[aria-label='upvote']")))
    upvote_button.click()
    downvote_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".voteButton[aria-label='downvote']")))
    downvote_button.click()
    save_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='save']")))
    save_button.click()
    # İşlemlerin başarıyla gerçekleştiğini kontrol etme
    assert upvote_button.get_attribute("aria-pressed") == "true"
    assert downvote_button.get_attribute("aria-pressed") == "true"
    assert save_button.get_attribute("aria-pressed") == "true"

def test_view_media(driver):
    driver.get("https://www.reddit.com/")
    # Bir gönderiye tıklama
    first_post = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Post")))
    first_post.click()
    # Medya öğelerini görüntüleme
    image = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img")))
    assert image.is_displayed()
    video = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "video")))
    assert video.is_displayed()

# Sprint 6 Testleri
def test_customization(driver):
    driver.get("https://www.reddit.com/settings/")
    # Profil özelleştirmesi
    # Kodu buraya tamamlayın

def test_user_blocking(driver):
    driver.get("https://www.reddit.com/settings/")
    # Kullanıcı engelleme
    # Kodu buraya tamamlayın

def test_feed_settings(driver):
    driver.get("https://www.reddit.com/settings/")
    # Besleme ayarları
    # Kodu buraya tamamlayın

def test_email_notifications(driver):
    driver.get("https://www.reddit.com/settings/")
    # E-posta bildirimleri
    # Kodu buraya tamamlayın

def test_localization(driver):
    driver.get("https://www.reddit.com/settings/")
    # Yerelleştirme
    # Kodu buraya tamamlayın
