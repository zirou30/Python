import tempfile
import urllib.request

def download_web_image(url):
    # Aqui esta definido .jpg mais ele baixa .png também.
    filename = tempfile.NamedTemporaryFile(prefix="", suffix=".jpg", dir=".", delete=False).name
    urllib.request.urlretrieve(url, filename)

url = input("Digite endereço da sua foto: ")
download_web_image(url)
