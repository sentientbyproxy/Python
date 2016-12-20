# This program makes an HTML image request using Pillow (the Python Image processing Library, or PIL),
# with Python 3.5.2.

import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://d13yacurqjgara.cloudfront.net/users/9745/screenshots/1555409/attachments/238245/Wallpaper.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image1.jpg"

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")
