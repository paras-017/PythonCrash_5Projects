import requests
url = 'https://www.youtube.com/playlist?list=PLt9sXaOeDEtOrmGppdXLQ6jZBNVLDK2SX'

def fetchandSaveFile(url, path):
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)

fetchandSaveFile(url, 'data/videos.html')