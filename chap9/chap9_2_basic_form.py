import requests
params = {'firstname': 'Doky', 'lastname': 'Kim'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)
