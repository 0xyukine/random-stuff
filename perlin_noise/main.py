import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise

axis = 255
image_array = np.zeros((axis,axis,3), np.uint8)

def gradient(ia):

    for x in range(255):
        for y in range(255):
            for z in range(3):
                ia[x,y,z] = y

    im = Image.fromarray(ia)
    return im

def 2d_noise(ia, increment=0.1, octaves=1, seed=1):

    noise = PerlinNoise()

    xoffset = 0
    yoffset = 0

    increment = 0.05

    for x in range(255):
        yoffset = 0
        for y in range(255):
            for z in range(3):
                ia[x,y,z] = noise([yoffset, xoffset]) * 255
            yoffset += increment
        xoffset += increment

    name = f"noise_{increment}_{octaves}_{seed}.png"
    im = Image.fromarray(ia)
    return im, name

im, name = 2d_noise(image_array)