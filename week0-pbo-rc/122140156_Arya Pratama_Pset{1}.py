height = int(input("Height : "))

gain = 1
col = 5
side = 0
for i in range(int(height)):
        print(" " * col, ("*" * gain) + "*" * side)
        gain += 1
        col -= 1
        side += 1