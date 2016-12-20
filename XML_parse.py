# This program will prompt for a URL, read the XML data from that URL 
# using urllib and then parse and extract the comment counts from the XML data,
# then compute the sum of the numbers in the file, using Python 2.7.12.


import urllib
import xml.etree.ElementTree as ET

#Prompt for the url.
# The url to be used is: http://python-data.dr-chuck.net/comments_312350.xml
url = raw_input('Please enter the url - ')
print 'Retrieving', url

# Read the XML data from that URL using urllib.
uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

# Look through the entire tree of XML using an XPath selector string.
counts = tree.findall('.//count')

# Compute the sum of the numbers in the file.
sum = 0
for count in counts:
    sum += int(count.text)

print 'Sum: ', sum
