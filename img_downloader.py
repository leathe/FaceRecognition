from bs4 import BeautifulSoup
import json
import urllib2
import os


def get_soup(_url, _header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(_url, headers=_header)), 'html.parser')

limit = 20
query = raw_input("Search for person: ") # You can change the query for the image here
image_type = "Image.1"
query = query.split()
query = '+'.join(query)
url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print url
# Add the directory for your image here
DIR = "Pictures"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

soup = get_soup(url, header)

ActualImages = []  # Contains the link for Large original images, type of image

# FIXME: Get the downloader to download exactly 10 images. If some downloads fail, skip them and continue.
# FIXME: Check that all images are proper and not corrupted. Delete corrupted images and download next.
for a in soup.find_all("div", {"class": "rg_meta"})[:limit]:
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    ActualImages.append((link, Type))

print "There are a total of ", len(ActualImages), " images to download."

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, "face".split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)

# Print images

for i, (img, Type) in enumerate(ActualImages):
    try:
        req = urllib2.Request(img, headers={'User-Agent': header})
        raw_img = urllib2.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print cntr
        if len(Type) == 0:
            f = open(os.path.join(DIR, image_type + "." + str(cntr)+".jpg"), 'wb')  # ".jpg"
        else:
            f = open(os.path.join(DIR, image_type + "." + str(cntr)+".jpg"), 'wb')  # Type

        f.write(raw_img)
        f.close()
    except Exception as e:
        print "Could not load: " + img
        print e

