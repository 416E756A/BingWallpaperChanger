import os
import random
from random import randint
import time

import re
import urllib2
from urllib2 import urlopen
import urllib
import cookielib
from cookielib import CookieJar
from bs4 import BeautifulSoup
cj=CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('Ueser-agent','Mozilla/5.0')]

wait_time=int(input("Enter interval time(minute) to Change Picture : "))
page='http://dailywallpaper.site88.net/Wallpaper/Bing/'
opened=True
while opened:
    try:
        urlopen=opener.open(page)
        source=urlopen.read()
        opened=False
    except:
        opened=True

find='<a href="(.*?)">.*</a>'
compiled=re.compile(find)
found=re.findall(compiled,source)
#print found
while True:
    #files=os.listdir('/home/alv3da/Pictures/Bing')
    index=random.randrange(0,len(found))
    urlopened=True
    t=True
    while urlopened==True and t!=False:
        try:
            t=urllib.urlretrieve("http://dailywallpaper.site88.net/Wallpaper/Bing/"+found[index],"temp.jpg")
            urlopened=False
        except:
            urlopened=True
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/alv3da/temp.jpg")
    #change the address of the file 
    time.sleep(wait_time*60)
    os.remove("/home/alv3da/temp.jpg")
    
    
              
