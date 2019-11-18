# We will scrap Index page from any website
# First we will search Google for Python PDFs
# The following google search code are as follows:-
# -inurl:(htm|html|php) intitle:"index of" + "last modified" +"parent directory" +description +size +(pdf) "python"
# #################################################################################################################
import requests
import re

f = open("INDEX_DATA.txt", "a+")
url=("https://pysnakeblog.blogspot.com/2019/10/web-scraping-using-python-index-page.html")             # Enter here Yours internet Page
website = requests.get(url)
html = website.text

#PDF
files = re.findall('href="(.*pdf)"', html)

for infile in sorted(x for x in (files)):
    f.write(url + infile+"\n")
f.close()
