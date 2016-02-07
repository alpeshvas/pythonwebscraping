import os
import fileinput
import sys
import shutil
import glob
from bs4 import BeautifulSoup
pathh='/home/appvash/Documents/iitg.vlab.co.in'
def depth3(patha,filename):
    fgh=os.path.join(patha,filename)
    try:
        f12=open(fgh,'r+')
        soup = BeautifulSoup(f12)
        for link4 in soup.findAll('link'):
                k6=link4['href']
                if not k6.startswith('http://'):
                    link4['href']="../../../"+link4['href']
                else:
                    link4['href']=link4['href'].replace("http://","../../../python2/")      
    
        for link5 in soup.findAll('img'):
                k8=link5['src']
                if not k8.startswith('http://'):
                    link5['src']="../../../"+link5['src']
                else:
                   link5['src']=link5['src'].replace("http://","../../../python2/")  
        for link in soup.findAll('a',href=True):
            href = link.get('href')
            if  href.startswith('http://'):
                link['href']=link['href'].replace("http://","../../../python2/")
                
            
        f12.close()
        html=soup.prettify("utf-8")
        with open(fgh,"wb") as file:
            file.write(html)
    except:
        return       
def depth2(patha,filename,n):
    fg=os.path.join(patha,filename)
    try:
        f1=open(fg,'r+')
        soup = BeautifulSoup(f1)
        for link in soup.findAll('a',href=True):
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
                if not href.startswith('http://'):
                    try:
                        os.rename(os.path.join(pathh,href),os.path.join(pathh,k))
                    except:
                        pass
                    link['href']=kkk 
                
                    try:
                        os.mkdir(g)
                    except:
                        pass
                    try:
                        shutil.copy(os.path.join(pathh,k),g)
                    except:
                        pass
                    depth3(g,k)
                else:
                   link['href']=link['href'].replace("http://","../../python2/") 
        for link3 in soup.findAll('link'):
                k6=link3['href']
                if not k6.startswith('http://'):
                    link3['href']="../../"+link3['href']
                else:
                    link3['href']=link3['href'].replace("http://","../../python2/")
                
        for link5 in soup.findAll('img'):
                k8=link5['src']
                if not k8.startswith('http://'):
                    link5['src']="../../"+link5['src']
                else:
                    link5['src']=link5['src'].replace("http://","../python2/")
        f1.close()
        html=soup.prettify("utf-8")
        with open(fg,"wb") as file:
            file.write(html)
    except:
        return       
def depth1(patha,filename,m):
    j=os.path.join(patha,filename)
    try:
        f2=open(j,'r+')
        soup = BeautifulSoup(f2)
        for link in soup.findAll('a',href=True):
                href = link.get('href') 
                k1=link.text
                k=k1.strip()+".html"
                o=link.text.strip()
            #print k
            #print href
                h=os.path.join(patha,href)
                kk=os.path.join(patha,k)
                kkk=o+"/"+k
                n=os.path.join(m,o)
                g=os.path.join(patha,o)
               # print h
                #print kk
                if not href.startswith('http://'):
                    try:
                        os.rename(os.path.join(pathh,href),os.path.join(pathh,k))
                    except:
                        pass
                    link['href']=kkk 
                    try:
                        os.mkdir(g)
                    except:
                        pass
                    try:
                        shutil.copy(os.path.join(pathh,k),g)
                    except:
                        pass
                    depth2(g,k,n)
                else:
                    link['href']=link['href'].replace("http://","../python2/")
        for link2 in soup.findAll('link'):
                k5=link2['href']
                if not k.startswith('http://'):
                    link2['href']="../"+link2['href']
                else:
                   link2['href']=link2['href'].replace("http://","../python2/") 
        for link5 in soup.findAll('img'):
                k8=link5['src']
                if not k8.startswith('http://'):
                    link5['src']="../"+link5['src']
                else:
                   link5['src']=link5['src'].replace("http://","../python2/")  
        f2.close()
        html=soup.prettify("utf-8")
        with open(j,"wb") as file:
            file.write(html)             
    except:
        print "chutiya error"
pathh='/home/appvash/Documents/iitg.vlab.co.in'
a='index.html'
def depth0(patha,filename):
    i=os.path.join(patha,filename)
    f1=open(i,'r+')
    soup = BeautifulSoup(f1)
    for link in soup.findAll('a',href=True):
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
            #print h
            #print kk
            if not href.startswith('http://'):
                try:
                    os.rename(h,kk)
                except:
                    pass
                link['href']=kkk  
                try:
                    os.mkdir(g)
                except:
                    pass
                try:
                    shutil.copy(kk,g)
                except:
                    pass
                depth1(g,k,o)
            else:
                link['href']=link['href'].replace("http://","python2/")
    f1.close()
    html=soup.prettify("utf-8")
    os.chdir(patha)
    with open("index.php","wb") as file:
        file.write(html)
depth0(pathh,a)
os.chdir(pathh)
filelist = glob.glob("*.html")
for f9 in filelist:
    os.remove(f9)           







    


    
