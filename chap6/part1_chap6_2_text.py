from urllib.request import urlopen
textPage = urlopen("http://www.scraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())
