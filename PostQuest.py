# I need a Python script to post questions to my website.
#! python3

import requests
import matplotlib.pyplot as plt
from time import sleep

i = 0
while True:
    f = open("questions.txt", "r")
    for x in f:
        url = 'https://www.w3schools.com/python/demopage.php'
        j = requests.post(url, data = x)
        print(x)
        sleep(5)
    f.close()

# open file
# read a line by line
# post a question on a web site
# sleep 60min
# take the next question
