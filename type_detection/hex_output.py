with open("image", "rb") as f:
    EOF = False
    while EOF is False:
        for x in range(8):
            for x in range(2):
                byte = f.read(1)
                if byte == b"":
                    EOF = True
                    break
                else:
                    print(byte.hex(), end="")
            print(" ", end="")
        #input()
        print()
