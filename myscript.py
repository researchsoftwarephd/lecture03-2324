from PIL import Image

img = Image.open('pisco.jpg')
img = img.rotate(45)
img.show()