import requests , bs4 , time , re ,os
from bs4 import BeautifulSoup as bSoup 
import xml , socket , json 
from tqdm import tqdm
from xml import etree
from xml.etree import ElementTree
from colorama import Fore , init
init()
lg = Fore.LIGHTGREEN_EX    # Colours
ly = Fore.LIGHTYELLOW_EX
lr = Fore.LIGHTRED_EX

def clear() :
    if os.name == 'nt':
        os.system('cls')
    else :
        os.system('clear')

banner = """
  █▀ █▀█ █▄ █ █▀▀   █▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄
  ▄█ █▄█ █ ▀█ █▄█   █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀
--------------------------------------------------------"""
tag = """     [+] Made By GH0STH4CK3R       [+] Version 1.0
--------------------------------------------------------"""

print(lg + banner)
print(ly + tag)

def rem_tags (st) :

    return ''.join(xml.etree.ElementTree.fromstring(str(st)).itertext())
print("\nType \'Help\' for instructions ")
print(ly + "")
search = input("\nSearch Song  : ")

if search == 'help' or search == 'Help' or search == 'HELP' or search == '-h' or search == '-H' :
    print("#----------------------- Help Menu -----------------------#\n")
    print("  Step [1] Search a song name")
    print("  Step [2] Type the correct number ")
    print("  Step [3] Song will be automatically downloaded\n")
    print("#----------------------------------------------------------#\n")
    input(" Press 'enter' to continue !")
    clear()
    import song_downloader
else :
    search = search.replace(' ','-')

url = "https://"+search+".mp3quack.cc/"

res = requests.get(url)       # Search

data = res.text 

page_soup = bSoup(data,"html.parser")  # Html web scraping

html = page_soup.find_all("div",{"class":"mf-content"})   # Finding content
links =page_soup.find_all("a",{"class":"unduhbtn"})    # Finding link
i = 0

print(lg + "")
for x in range(len(html)) :
    h31 = html[x]
    h3 = h31.find_all("h3")
    ttt = str(h3[0]).replace('<h3>','')
    title = ttt.replace('</h3>','')
    if '<a' in title :
        soup = bSoup(title,"html.parser")
        title=(soup.a.string)
    if title=="" or title==" " :
        title = '[ No Title ]'
    i += 1
    #Aras.h ft. helena Love Songs| Broken Angel | Pure Love | One Night in Dubai 
    
    print(' [',i,'] ',title)
    time.sleep(0.2)    

tno = int(input('\n\nEnter Song Number : '))

c_link = links[tno-1]['href']

rurl = url+'convert/'

ytcode = c_link.replace(rurl,'')      # Youtube video ID

ytlink = "https://www.youtube.com/watch?v="+ytcode   #https://www.youtube.com/watch?v=papuvlVeZg8

# ---------------------------------------------------------------------------- HTTP REQUEST NO 1

url1 = "https://yt1s.com/api/ajaxSearch/index"

data = {"q": ytlink,"vt": "mp3"}

r = requests.post(url1,data=data)

response =  json.loads(r.text)

vid = response['vid']                # Get video id
k = response['kc']
title = response['title']            # Get title
a_rtist = response['a']
print(lg+"\nTitle    : ",title)
print("Uploader : ",a_rtist)

# ---------------------------------------------------------------------------- HTTP REQUEST NO 2

url2 = "https://yt1s.com/api/ajaxConvert/convert"

data = {"vid": vid,"k": k}

r2= requests.post(url2,data=data)
# ------------------------------------------------ Spinner
import sys
import time

print(ly+"")
def spinning_cursor():

    cs = ['Converting /','Converting -','Converting \\','Converting |']

    while True:
        for cursor in cs :
            yield cursor

spinner = spinning_cursor()
for _ in range(20):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b')    
#sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b') 

res = json.loads(r2.text)

dlink = res['dlink']              # Get download url
#print(res)


# ---------------------------------------------------------------------------- HTTP REQUEST NO 3

url3 = dlink

params = {"file": dlink}

r3 = requests.get(url3,stream=True)

tnm = str(title)
songname = tnm+".mp3"

rcode = r3.status_code              
print(lg+"")
if rcode == 200 :
    
    total = int(r3.headers.get('content-length', 0))   # Progressbar
    with open(songname, 'wb') as file, tqdm(
            desc=songname,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in r3.iter_content(chunk_size=1024):
            size = file.write(data)                     # Downloading
            bar.update(size)
    print("\nDownloaded > ",songname)        
    input("")
else :
    print("Download failed ! ",rcode)    
