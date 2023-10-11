import os, sys

PNG = [137,80,78,71,13,10,26,10]
JPG = [255, 216]
GIF = [71, 73, 70]

path = input()
dirs = os.listdir(path)

for file in dirs:
    ffile = path + "/" + file
    with open(ffile, "rb") as f:
        header = []
        for x in range(8):
            byte = f.read(1)
            header.append(int.from_bytes(byte, byteorder="big"))
        print(header)
        if set(PNG).issubset(header):
            print("png")
            os.rename(ffile, ffile + ".png")
        elif set(JPG).issubset(header):
            print("jpg")
            os.rename(ffile, ffile + ".jpg")
        elif set(GIF).issubset(header):
            print("gif")
            os.rename(ffile, ffile + ".gif")
