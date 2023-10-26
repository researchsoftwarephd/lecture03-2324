from PIL import Image

def load_and_rotate(filename):
    img = Image.open(filename)
    return img.rotate(45)