import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.uol.com.br/')
except urllib.error.URLError:
    print('Deu erro. O site não está acessível no momento.')
else:
    print('Site acessado com sucesso.')
