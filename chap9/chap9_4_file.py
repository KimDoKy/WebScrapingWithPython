import requests

files = {'uploadFile': open('../files/docker-logo.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)
