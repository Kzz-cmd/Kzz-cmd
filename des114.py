import urllib.request
try:
    site = urllib.request.urlopen('http://www.youtube.com.br')
except:
    print('não deu')
else:
    print('tudo ok')