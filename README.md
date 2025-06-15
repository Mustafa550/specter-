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
==============================================
      Specter Toolkit - Hızlı Kurulum Rehberi
==============================================

1) GitHub reposunu klonlayın veya dosyayı indirin:

   git clone https://github.com/Mustafa550/specter.git
   cd specter

2) Gerekli Python modüllerini yükleyin:

   pip install -r requirements.txt

   *requirements.txt içeriği:*
   rich
   colorama
   requests
   shodan

3) (Opsiyonel) Ek araçları yükleyin:

   Termux için:
      pkg install hydra crunch

   Ubuntu/Debian için:
      sudo apt update
      sudo apt install hydra crunch

4) Scripti çalıştırın:

   python3 specter.py

5) Program açıldığında menüden istediğiniz aracı seçerek kullanabilirsiniz.

==============================================

Not:  
- Shodan API kullanımı için https://account.shodan.io/ üzerinden ücretsiz API anahtarı alın.  
- Phishing sayfalarını dış dünyaya açmak için ngrok veya benzeri tünel araçlarını kullanabilirsiniz.  
- Araç yalnızca etik amaçlı kullanım içindir, izinsiz kullanımı yasaktır.

==============================================
"""
