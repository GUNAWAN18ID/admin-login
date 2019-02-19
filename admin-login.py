#mau ngapain monyet?
#recode?
#recode gak akan buat lu menjadi pro bangsat !!!
#jauh jauh lu sana babi


from urllib.request import urlopen, Request, URLError, HTTPError
import sys
import time
print('''\033[93m
     _       _           _         _             _       
    / \   __| |_ __ ___ (_)_ __   | | ___   __ _(_)_ __  
   / _ \ / _` | '_ ` _ \| | '_ \  | |/ _ \ / _` | | '_ \ 
  / ___ \ (_| | | | | | | | | | | | | (_) | (_| | | | | |
 /_/   \_\__,_|_| |_| |_|_|_| |_| |_|\___/ \__, |_|_| |_|
                                           |___/         
''')
def hp(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(10./100)
hp("\033[92mTools   : Admin Finder V 0.1")
hp("Created : 19 feb 2019")
hp("Author  : Junior404")
hp("Blogger : www.gunawanid.me")
hp("Team    : 407 Authentic eXploit")
hp("Youtube : youtube.com/c/GUNAWANID")
hp("Spesial Thanks To : Jax BCD\033[0m")
header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
file = open('word.txt', 'r').read().split('\n')
site = input('\033[95mMasukan Link: ')
hp("\033[94mMencari Admin Login...\033[0m")
for list in file:
    url = site + '/' +list
    try:
        req = Request(url, None, header)
        res = urlopen(req)
    except(ValueError, HTTPError, URLError):
        print('\033[31;1mTidak Ditemukan: ' + url + '\033[0m')
    else:
        print('\033[32;1mBerhasil Ditemukan: ' + url + '\033[0m')
