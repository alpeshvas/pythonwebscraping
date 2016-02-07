import os
import fileinput
import sys
import shutil
import re
from bs4 import BeautifulSoup
os.chdir('/home/appvash/Desktop/iitg.vlab.co.in')
pathh='/home/appvash/Desktop/iitg.vlab.co.in'
f=open('index.html','r+').read()
soup = BeautifulSoup(f)
for link in soup.findAll('a'):
            href = link.get('href') 
            k=link.text+".html"
            o=link.text
            #print k
            #print href
            h=os.path.join(pathh,href)
            kk=os.path.join(pathh,k)
            kkk=o+"/"+k
            print h
            print kk
            #try:
                #os.rename(h,kk)
            #except:
             #   pass
            replaceall(i,href,kkk)
          # try:
            #    os.mkdir(os.path.join(pathh,o))
            #except:
             #   pass
            #try:
             #   shutil.move(kk,os.path.join(pathh,o))
            #except:
             #   pass
            

