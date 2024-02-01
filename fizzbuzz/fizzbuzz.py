x = 0
while True:
    out = f"{x}: "
    if x % 3 == 0:
        out += "fizz"
    if x % 5 == 0:
        out += "buzz"
    input(out)
    x += 1
