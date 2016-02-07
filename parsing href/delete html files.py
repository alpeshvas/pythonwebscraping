import glob, os
os.chdir('/home/appvash/Desktop')
filelist = glob.glob("*.html")
for f in filelist:
    os.remove(f)
