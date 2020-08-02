import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&t=0s')
except:
    print('Deu Erro!')
else:
    print('Deu Certo!')
    print(site.read())
