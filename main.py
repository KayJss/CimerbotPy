import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import classes
#Değişken İsimlerini Ellemeyin
driver = webdriver.Chrome()
url = classes.web.link #Url classes.py Dosyasından Çekiliyor
driver.get(url) # Url Alınıyor
# Tc kimliği girilmesi için bekleniyor
trid_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'tridField')) # Tc No Girilecek Yeri Belirleniyor
)
trid_input.send_keys(classes.web.tc# Tc Kimliği Giriliyor
time.sleep(5) # 5 Saniye Bekleniyor
egp_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'egpField')) #E-Devlet şifresinin girelecek Yeri Belirleniyor
)
egp_input.send_keys(classes.web.sifre) #E devlet şifresi giriliyor
time.sleep(5) #5 Saniye bekletiliyor
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'submitButton'))
)
submit_button.click();time.sleep(5) #buna tıkladıktan sonra bekleniyor

time.sleep(5) #5 Saniye Beklet
driver.quit() # Chrome'dan çık
print("Çıkılıyor")
