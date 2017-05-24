from pytube import YouTube
import urllib
import urllib2
from bs4 import BeautifulSoup

print "Enter video name:",
_input = raw_input()
youtube_link = 'https://www.youtube.com'
linkArray = []
query = urllib.quote(_input)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
    if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
        linkArray.append(vid['href'])

complete_link = youtube_link + linkArray[1]
print complete_link
yt = YouTube(complete_link)
yt.set_filename("video")
video = yt.get('mp4', '360p')
video.download('')
