# from PIL import Image
import sys
import argparse
import os

# ###UTILS###


# def resize(image_name: str, width: int, height: int, new_name: str = None):
#     if new_name == None:
#         new_name = image_name + "(1)"
#     img = Image.open(image_name)
#     img = img.resize((width, height), Image.Resampling.LANCZOS)
#     img.save(new_name)


# def resize(image: str, newName: str = None):
#     myImg = Image.open(image)
#     myImg = myImg.convert('LA')
#     width, height = myImg.size
#     ratio = int(width/200)
#     width = 200
#     height = int(height/ratio)
#     myImg = myImg.resize((width, height))
#     myImg.save(newName)


# def printImg(imgArr):
#     for i in range(len(imgArr)):
#         for j in range(len(imgArr[0])):
#             print(imgArr[i][j], end="")
#         print("")


# myImg = Image.open(sys.argv[1])
# resize(sys.argv[1], "bwimg.png")
# newImg = Image.open("bwimg.png")
# newImg = newImg.convert('RGB')
# size = newImg.size

# asciiArr = []
# charArr = []

# for i in range(size[0]):
#     asciiArr.append([])
#     for j in range(size[1]):
#         pixelVal = newImg.getpixel((i, j))
#         asciiArr[i].append((pixelVal[0] + pixelVal[1] + pixelVal[2])/3)


# for i in asciiArr:
#     newArr = []
#     for j in i:
#         x = ""
#         if j > 229.5:
#             x = " "
#         elif j < 229.5 and j > 204:
#             x = "."
#         elif j < 204 and j > 178.5:
#             x = ":"
#         elif j < 178.5 and j > 153:
#             x = "-"
#         elif j < 153 and j > 127.5:
#             x = "="
#         elif j < 127.5 and j > 102:
#             x = "+"
#         elif j < 102 and j > 76.5:
#             x = "*"
#         elif j < 76.5 and j > 51:
#             x = "#"
#         elif j < 51 and j > 25.5:
#             x = "%"
#         else:
#             x = "@"

#         newArr.append(x)

#     charArr.append(newArr)

# rotated = list(reversed(list(zip(*charArr))))
# rotated = list(reversed(list(zip(*rotated))))
# rotated = list(reversed(list(zip(*rotated))))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("filename")
parser.add_argument("-n", "--new-filename")
parser.add_argument("-r", "--ratio")
parser.add_argument("-w", "--width")
parser.add_argument("-h", "--height")


def validate_args(args: argparse.Namespace):
    if args.ratio and (args.width or args.height):
        print(
            "Invalid arguments: if you specify a ratio, you can't specify width and height!")
        sys.exit(1)

    if (args.width == None) != (args.height == None):
        print("Invalid arguments: either width and height must both be specified, or neither of them can be!")
        sys.exit(1)

    if not os.path.exists(args.filename):
        print("File does not exist!")
        sys.exit(1)


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    validate_args(args)
