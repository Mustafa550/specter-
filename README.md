Specter Toolkit

Merhaba! Ben Mustafa550, Specter Toolkit ile beyaz şapkalı hackerlar ve siber güvenlik meraklıları için kapsamlı ve kullanımı kolay bir etik hacking aracı seti hazırladım.

Bu araç sayesinde;

Web uygulamalarını test edebilir,

SQL Injection, XSS gibi zafiyetleri keşfedebilir,

Phishing sayfaları oluşturup eğitim amaçlı kullanabilir,

Brute force ve port tarama yapabilir,

OSINT ve güvenlik başlıkları gibi birçok alanı inceleyebilirsiniz.


Specter, Termux ve Linux tabanlı sistemlerde sorunsuz çalışır ve tüm araçları tek bir script içinde barındırır.

Neden Specter?

Modüler ve kullanıcı dostu menüler,

Renkli ve anlaşılır arayüz,

Zengin özellik seti,

Kolay kurulum ve hızlı kullanım.


Kimler için?

Bu proje etik hackerlar, siber güvenlik öğrencileri ve bilgi güvenliği alanında çalışan profesyoneller içindir.
Kötü niyetli kullanımlardan uzak durun, etik kalın!


---

Her türlü soru ve öneri için GitHub Issues bölümünü kullanabilirsiniz.
İyi çalışmalar!


"""
============================================
    Specter Toolkit - Kurulum ve Kullanım
============================================

1. Gereksinimler:
   - Python 3.6 veya üzeri
   - pip (Python paket yöneticisi)
   - Termux (Android) veya Linux ortamı
   - Hydra (brute-force için, opsiyonel)
   - Crunch (wordlist oluşturmak için, opsiyonel)

2. Gerekli Python modüllerini yükleyin:
   pip install rich colorama requests shodan

3. Hydra ve Crunch yüklemek için:

   Termux:
      pkg install hydra crunch

   Ubuntu/Debian:
      sudo apt update
      sudo apt install hydra crunch

4. Scripti çalıştırmak için terminalden:
   python3 specter_alliance.py

5. Program açıldıktan sonra menüden seçim yaparak araçları kullanabilirsiniz.

6. Shodan API kullanmak için:
   https://account.shodan.io/ adresinden ücretsiz API anahtarınızı alın.

7. Phishing modülünde oluşturduğunuz sayfayı dışarıdan erişilebilir yapmak için
   ngrok gibi bir tünel aracı kullanmanızı öneririz.

=======================================
