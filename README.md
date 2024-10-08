

## CimerbotPy V2.3 Gereksinimler

- Python 3.x
- `requirements.txt` dosyasındaki gerekli kütüphanelerin yüklenmesi
- `classes.py` dosyasına TC Kimlik Numaranızı ve e-devlet şifrenizi girmeniz gerekmektedir.

## Kurulum

Projenin çalıştırılması için aşağıdaki adımları izleyin:

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/KayJss/cimerbotpy.git
   ```
2. **Klonlanan Dizine Girin**:
   ```bash
   cd cimerbotpy
   ```
3. **Gerekli Kütüphaneleri Yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Programı Çalıştırın**:
   ```bash
   python main.py
   ```

## Kullanım

1. `classes.py` dosyasını açın ve aşağıdaki bilgileri girin:
   - TC Kimlik Numaranız
   - E-devlet şifreniz
   - Mail Adresiniz
   - Başvuru Metni
   - Max Karakter
   - Min Karakter

2. Programı başlattığınızda, otomatik olarak e-devlet hesabınıza giriş yapılacaktır.

3. **Otomatik Şikayet** Belirli bir Olayı Otomatik olarak Şikayet Edebilirsiniz.

4. **Not**: E-devletinizde İki Aşamalı doğrulamayı(2FA) Aktif Etmeniz Gerekmektedir Yoksa **Kullanamazsınız**

## Geliştirme Planları

- **Otomatik Şikayet Özelliği**: Kullanıcıların Cimer üzerinden otomatik şikayet oluşturabilmesi için gerekli geliştirmeler yapılacaktır.
- **Hata Ayıklama ve İyileştirme**: Kullanıcı geri bildirimlerine dayalı olarak hataların giderilmesi ve uygulamanın iyileştirilmesi hedeflenmektedir.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Depoyu fork edin.
2. Yeni bir dal oluşturun (`git checkout -b feature/ÖzellikAdı`).
3. Değişikliklerinizi ekleyin (`git commit -m 'Yeni özellik ekle'`).
4. Dala gönderin (`git push origin feature/ÖzellikAdı`).
5. Bir pull isteği oluşturun.

## Lisans

Bu proje GNU General Public License Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.
