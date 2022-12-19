from PIL import Image
import numpy as np

img = Image.open("buffer/微信图片_20221217192722.jpg")
# img.show()
w, h = img.size
padding = (h - w) // 2

# img_padded = np.zeros(shape=(w, h, 3), dtype=np.uint8)
# img_padded[:, padding:padding+w, :] = img
# img_array = np.rot90(img_padded, 1)
img_array = np.asarray(img)
img_array = np.rot90(img_array, 1)
img = Image.fromarray(img_array)
img.thumbnail((1600, 1200), Image.Resampling.LANCZOS)
# img = img.resize((h, w))
# img.show()
print(img.size)

new_image = Image.new('RGB', (2000, 2000), 'white')
new_image.paste(img, (0, 0, img.size[0], img.size[1]))
new_image.save("output.jpg")
