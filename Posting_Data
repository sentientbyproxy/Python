# Posting data into a web form, using Python 3.5.2.

import requests

my_data = {"name": "Joel", "email": "jtguros@hotmail.com"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data = my_data)

f = open("myfile.html", "w+")
f.write(r.text)
