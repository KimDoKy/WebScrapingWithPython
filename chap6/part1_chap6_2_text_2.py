from urllib.request import urlopen
textPage = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(textPage.read())
