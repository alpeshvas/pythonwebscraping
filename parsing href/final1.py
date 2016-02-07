import os
import fileinput
import sys
import shutil
import glob
from bs4 import BeautifulSoup
pathh='/home/appvash/Desktop'
def depth0(patha,filename):
    j=os.path.join(patha,filename)
    try:
        f1=open(j,'r+')
        soup = BeautifulSoup(f1)
        for link in soup.findAll('a'):
                href = link.get('href')
                k1=link.text
                k=k1.strip()+".html"
                o=link.text.strip()
            #print k
            #print href
                h=os.path.join(patha,href)
                kk=os.path.join(patha,k)
                kkk=o+"/"+k
                g=os.path.join(patha,o)
               # print h
                #print kk
                #try:
                 #   os.rename(os.path.join(pathh,href),os.path.join(pathh,k))
                #except:
                    #pass
                link['href']=kkk 
                
                #try:
                #    os.mkdir(g)
                #except:
                 #   pass
                #try:
                 #   shutil.copy(os.path.join(pathh,k),g)
                #except:
                 #   pass
        for link2 in soup.findAll('link'):
                k5=link2['href']
                link2['href']="../"+link2['href']


                
        f1.close()
        html=soup.prettify("utf-8")
        os.chdir(patha)
        with open(j,"wb") as file:
            file.write(html)
    except:
        pass

depth0(pathh,"index.html")
