import requests
from bs4 import BeautifulSoup
def proxy1():

    r = requests.get('https://cagriari.com/fresh_proxy.txt')
    soup = BeautifulSoup(r.content,"lxml")
    a=soup.find_all('body')
    for i in a:
        a=i.text
        x=a.replace("# https://github.com/sh4dowb/proxy-scraper", "")
        print(x)
        print("yazdırıldı")
        dosya=open("proxy.txt","a",encoding="utf-8")
        dosya.write(str(x))
        dosya.close()
def proxy2():
    import requests
    from bs4 import BeautifulSoup
    r = requests.get("http://spys.me/proxy.txt")
    soup = BeautifulSoup(r.content, "lxml")
    spy=soup.find_all('body')
    for i in spy:
        a=i.text
    x=print(a.replace('''Mirrors=http://spys.me/proxy.txt https://twitter.com/spys_one https://t.me/spys_one
Support by donations:
BTC 1H1ZH7WJVzU7GMDSwsAQrqvGrbLY49wdae
ETC 0xd1Cf57E35003aD846524a7778D99e8856B96C241
BCH 19o72EjQw3mEYNciZ4JxvpDmUbjjtXghBb
LTC LMrLZNWGYK3kMHvyioBqZdXYWE3pKj7xZX
IP address:Port Country-Anonymity(Noa/Anm/Hia)-SSL_support(S)-Google_passed(+)''', 't.me/hasario iletişime gecebılırsınız   '))
    dosya = open("proxy.txt", "a", encoding="utf-8")
    dosya.write(str(x))
    dosya.close()





proxy2()
proxy1()
