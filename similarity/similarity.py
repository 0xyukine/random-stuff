from PIL import Image
import imagehash
import os

def Similarity(a, b, path=""):
    phash = imagehash.average_hash(Image.open(path + a)) - imagehash.average_hash(Image.open(path + b))
    return phash

#Currently assumes images directory in the same directory as source code
#Compares every file in images directory with every other file resulting in redundant checks

path = "./images/"
idir = os.listdir(path)
for image in idir:
    for oimage in idir:
        if oimage != image:
            print(image, oimage)
            print(Similarity(image, oimage, path))