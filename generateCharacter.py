def generateDictionary():
    # read file
    fin = open("font3.txt", "r")
    lc = 1
    moveOn = 1
    while (moveOn == 1):
        for line in fin:
            # value configuration
            num = line[2:-3]
            v = str(num).encode('utf8')
            value = list(bin(int(v, 16))[2:].zfill(8))
            # key configuration
            key = line[-2]
            # Dictionary
            dicts = {}
            dicts[key]=value

            moveOn = 1
        lc = lc + 1
    fin.close()


# generateDictionary()

# Display character
def displayObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            if (x+j>=123 or x+j<0):
                break
            if (y+i>=64 or y+i<0):
                break
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1
    lcd.show()

# character =
# displayObject(generateDictionary(),10,10)




