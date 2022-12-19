from PIL import Image
import numpy as np
from utils.util_image import *

img = Image.open("buffer\微信图片_20221217192722.jpg")
# img.show()
img = rotate_pic(img)
print(img.size)
# img.thumbnail((1600, 1200), Image.Resampling.LANCZOS)
img = img.resize((1600, 546))
print(img.size)

new_image = Image.new('RGB', (2000, 2000), 'white')
new_image.paste(img, (0, 0, img.size[0], img.size[1]))
new_image.save("output.jpg")
