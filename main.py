import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from tkinter import messagebox
import sys
import classes

try:
    
    
    # Başvuru metninin uzunluğunu kontrol et
    if classes.web.min_karakter < classes.web.basvuru_karakter < classes.web.max_karakter:
        driver = webdriver.Chrome()
        url = classes.web.link  # URL classes.py dosyasından alınıyor
        driver.get(url)  # URL'ye git

        try:
            time.sleep(3)  # Sayfanın yüklenmesini bekleyin
            
            # TC Kimlik numarasını gir
            trid_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'tridField'))
            )
            trid_input.send_keys(classes.web.tc)

            # EGP Şifresini gir
            egp_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'egpField'))
            )
            egp_input.send_keys(classes.web.sifre)

            # Gönder butonuna tıklayın
            submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, 'submitButton'))
            )
            submit_button.click()

            root = tk.Tk()
            root.withdraw()  # Ana pencereyi gizle

            # Sayfa kaynağını kontrol et
            page_source = driver.page_source
            if "e-Devlet kapısı hesabınızda aktif olmadığından dolayı CİMER'e giriş yapamamaktasınız" in page_source:
                messagebox.showerror("İşlem Başarısız", "İki aşamalı giriş özelliği aktif değil, işlem yapılamıyor.")
                driver.quit()
                exit()

            messagebox.showinfo("Bilgilendirme", "180 saniye içinde SMS olarak gelen kodu girmezseniz program sona erecektir.")
            start_time = time.time()
            timeout = 180

            while True:
                current_url = driver.current_url
                page_source = driver.page_source

                if "Bir hata oluştu! Teknik bir hata ile karşılaştınız! Hata bilgisini aldık." in page_source:
                    messagebox.showerror("Hata", "Bir hata oluştu! Program kapatılıyor.")
                    driver.quit()
                    sys.exit()

                if current_url == "https://www.cimer.gov.tr/Basvuru":
                    print("CİMER sayfasına yönlendirildi, duruyor...")
                    break

                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    messagebox.showwarning("Uyarı", "Zamanında giriş yapılmamıştır.")
                    driver.quit()
                    sys.exit()

                time.sleep(1)

            time.sleep(20)  # Sayfanın yüklenmesini bekleyin


            # E-posta bilgilerini gir
            eposta_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'BasvuruVatandas_Eposta'))
            )
            eposta_input.send_keys(classes.web.mail)

            # E-posta tekrar bilgilerini gir
            eposta_tekrar_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'BasvuruVatandas_EpostaTekrar'))
            )
            eposta_tekrar_input.send_keys(classes.web.mail)


            ileri = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'btnIleri')))
            ileri.click()
            
            # Başvuru metnini gir
            basvuru_metin_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'Basvuru_Metin'))
            )
            basvuru_metin_input.send_keys(classes.web.basvuru_metin)

            ileri = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'btnIleri')))
            ileri.click()

            # Kullanıcı sözleşmesini kabul et
            sozlesme_checkbox = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'chkKullaniciSozlesmesi'))
            )

            # JavaScriptExecutor kullanarak checkbox'a tıklama
            driver.execute_script("arguments[0].click();", sozlesme_checkbox)

            # Başvuruyu tamamla butonuna tıklama
            tamamla_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'btnBasvuruyuTamamla'))
            )
            tamamla_button.click()  # Tıklama

        except Exception as e:
            print("Bir hata oluştu:", repr(e))

        finally:
            driver.quit()
            print("Çıkılıyor")
    else:
        print("Başvuru metni uzunluğu uygun değil.")
        print(classes.web.basvuru_karakter)
except Exception as e:
    print("Ana hata:", repr(e))
