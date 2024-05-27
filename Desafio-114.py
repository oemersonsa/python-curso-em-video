import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.request.URLError:
    print('O site pudim não está acessível no momento!')
else:
    print('O site pudim está acessível!')

