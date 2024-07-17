import requests
import time

def check_version(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            remote_version = response.text.strip()
            with open('tool_version.txt', 'r') as f:
                local_version = f.read().strip()
            
            if remote_version != local_version:
                print(f"Yeni güncelleme mevcut: {remote_version}! Lütfen güncelleyin.")
                time.sleep(1)
                webbrowser.open('https://github.com/softwarEWA/Efuscater')
            else:
                print("Program güncel.")
                time.sleep(3)
        else:
            print(f"Hata: {response.status_code}")
    except requests.RequestException as e:
        print(f"Hata: {e}")

url = "https://github.com/softwarEWA/Efuscater/raw/main/tool_version.txt"
check_version(url)
