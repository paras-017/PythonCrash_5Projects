import requests
url = "https://www.python.org/"

def fetchandSaveFile(url, path):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    with open(path, 'w') as f:
        f.write(r.text)

fetchandSaveFile(url, 'data/videos.html')