import urllib.request

def download(url):
    site = urllib.request.urlopen(url)
    texto = site.read() .decode("iso8859")
    save = open("nomes.txt ", "x")
    save.write(texto)
    save.close()

url = input("Url do arquivo: ")
download(url)
