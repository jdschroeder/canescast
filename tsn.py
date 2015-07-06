import urllib2
import re

urlStr = 'http://www2.tsn.ca/podcasts/tsnradiopodcast.xml'

fileHandle = urllib2.urlopen(urlStr)
str1 = ""
x = 0
while(x < 100):
  line = fileHandle.readline()
  str1 += line
  search = re.search("</item>", line)
  if search:
    x+=1
  
fileHandle.close()
str1 += "</channel></rss>"  
str1.replace('\n', ' ')

#print str1
f = open('tsn.xml','w')
f.write(str1)
f.close()
