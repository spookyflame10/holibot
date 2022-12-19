import wikipedia
import sys
import time, random
from datetime import date
import urllib.request
from PIL import Image
from datetime import date
import tweepy as t
import tempfile
dirpath = tempfile.mkdtemp()

auth = t.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, token, token_secret)
api = t.API(auth)

str = wikipedia.WikipediaPage(title=wikipedia.search(date.today().strftime("%B %d"),1)[0]).section("Holidays and observances")
list2 = str.split('\n')
list3 = []
for x in list2:
    string2 = ''
    if ('Day' in x) or ('day' in x):
        for y in x.split():
            string2 += y + " "
            if y== 'day' or y == 'Day':
                break
        list3.append(x)
    else:
        continue
randomitem = random.choice(list3)
page2 = wikipedia.WikipediaPage(wikipedia.search(randomitem,1)[0])
while(page2.title not in list3):
    randomitem = random.choice(list3)
    page2 = wikipedia.WikipediaPage(wikipedia.search(randomitem,1)[0])
listresult = page2.summary.split('.')
summary = listresult[0]
if len(summary)>200:
    summary = summary[0:200]+ "..."
count =0
for x in page2.images:
    if x.endswith('.svg'):
        continue
    else:
        count +=1
if count != 0:
    for x in page2.images: 
        if x.endswith('.svg'):
            continue
        else:
            urllib.request.urlretrieve(x,dirpath +"\img.png")
            img = Image.open(dirpath +"\img.png")
            img.show()
            break
    mo = api.media_upload(dirpath +"\img.png")
    hi = api.update_status(status = "#Today is " + page2.title + "! " + summary, media_ids = [mo.media_id])
    api.update_status(status = "@Iae101Silee Wikipedia Link: " + page2.url, in_reply_to_status_id = hi.id)
else:
    hi = api.update_status(status = "#Today is " + page2.title + "! " + summary)
    api.update_status(status = "@Iae101Silee Wikipedia Link: " + page2.url, in_reply_to_status_id = hi.id)

