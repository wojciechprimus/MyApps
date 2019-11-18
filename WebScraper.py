# Web scraping index page and converting image url to html thumbnail webpage
# Create by Joel Dcosta
# Check out my other web scraping videos uploaded previously
# ##########################################################################
import requests
import re

url=("https://pysnakeblog.blogspot.com/2019/10/web-scraping-using-python-index-page.html")             # Enter here Yours internet Page

f = open("py3 Scrap image.html", "a+",encoding='utf-8')

website = requests.get(url)
html = website.text

#jpg
files = re.findall('href="(.*jpg)"', html)

#print sorted(x for x in (files))
for infile in sorted(x for x in (files)):
   #using html image tags <img src="IMAGE_URL" width='200' height='133
   f.write("<img src='")
   f.write(url + infile)
   f.write("' width='200' height='133'>")

f.close()
