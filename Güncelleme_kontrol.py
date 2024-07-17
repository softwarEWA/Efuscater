import requests

def check_version(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            remote_version = response.text.strip()
            with open('tool_version.txt', 'r') as f:
                local_version = f.read().strip()
            
            if remote_version != local_version:
                print(f"Yeni güncelleme mevcut: {remote_version}! Lütfen güncelleyin.")
            else:
                print("Program güncel.")
        else:
            print(f"Hata: {response.status_code}")
    except requests.RequestException as e:
        print(f"Hata: {e}")

# URL'nizi buraya yapıştırın
url = "https://github.com/softwarEWA/Efuscater/raw/main/tool_version.txt"
check_version(url)
