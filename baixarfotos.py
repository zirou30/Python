import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"              #Aqui esta definido .jpg mais ele baixa .png também.
    urllib.request.urlretrieve(url, full_name)

a = input ("Digite endereço da sua foto: ")     
download_web_image(a)
