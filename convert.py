from PIL import Image
import sys

###UTILS###
def resize(image, newName):
    myImg = Image.open(image)
    myImg = myImg.convert('LA')
    width, height = myImg.size
    ratio = int(width/200)
    width = 200
    height = int(height/ratio)
    myImg = myImg.resize((width, height))
    myImg.save(newName)

def printImg(imgArr):
    for i in range(len(imgArr)):
        for j in range(len(imgArr[0])):
            print(imgArr[i][j], end="")
        print("")

myImg = Image.open(sys.argv[1])
resize(sys.argv[1], "bwimg.png")
newImg = Image.open("bwimg.png")
newImg = newImg.convert('RGB')
size = newImg.size

asciiArr = []
charArr = []

for i in range(size[0]):
    asciiArr.append([])
    for j in range(size[1]):
        pixelVal = newImg.getpixel((i,j))
        asciiArr[i].append((pixelVal[0] + pixelVal[1] + pixelVal[2])/3)
print(asciiArr)

for i in asciiArr:
    newArr = []
    for j in i:
        x = ""
        if j > 229.5:
            x = " "
        elif j < 229.5 and j > 204:
            x = "."
        elif j < 204 and j > 178.5:
            x = ":"
        elif j < 178.5 and j > 153:
            x = "-"
        elif j < 153 and j > 127.5:
            x = "="
        elif j < 127.5 and j > 102:
            x = "+"
        elif j < 102 and j > 76.5:
            x = "*"
        elif j < 76.5 and j > 51:
            x = "#"
        elif j < 51 and j > 25.5:
            x = "%"
        else:
            x = "@"

        newArr.append(x)

    charArr.append(newArr)

rotated = list(reversed(list(zip(*charArr))))
rotated = list(reversed(list(zip(*rotated))))
rotated = list(reversed(list(zip(*rotated))))

print(rotated)
printImg(rotated)


