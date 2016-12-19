# A program to parse JSON data, written in Python 2.7.12.

import urllib
import json


# Prompt for a URL.
# The URL to be used is:  http://python-data.dr-chuck.net/comments_312354.json
url = raw_input("Please enter the url: ")
print "Retrieving", url

# Read the JSON data from the URL using urllib.
uh = urllib.urlopen(url)
data = uh.read()

# Parse and extract the comment counts from the JSON data.
js = json.loads(str(data))

# Set starting point of sum.
sum = 0

comments = js["comments"]

# Compute the sum of the numbers in the file.
for item in js["comments"]:
    sum += item["count"]

# Enter the sum below:
print "Sum: ", sum
