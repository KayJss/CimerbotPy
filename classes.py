class web:
    const link = "https://www.cimer.gov.tr/Hesap/EDevletGiris" #Elleme
    tc = "" #Tc Kimlik Numaranı gir
    sifre = "" #E devlet Şifreni Gir
    mail = "" #Mailinizi Girin
    basvuru_metin = """         """ #Başvuru metni
    max_karakter = 5999 #Maksimumum Karakter
    min_karakter = 1000 #Minimum Karakter
    basvuru_karakter = len(basvuru_metin) #Başvuru metninin içerdiği Toplam Karakter Sayısı (boşluklar vesaire Dahil)
