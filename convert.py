from PIL import Image
import sys
import argparse
import os


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("filename")
parser.add_argument("-n", "--new-filename")
parser.add_argument("-r", "--ratio")
parser.add_argument("-w", "--width")
parser.add_argument("-h", "--height")
parser.add_argument("-s", "--gaps", action=argparse.BooleanOptionalAction)


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


def create_new_filename(filename: str) -> str:
    if filename.startswith(".\\"):
        filename = filename[2:]
    filename_no_extension = filename.split(".")[0]
    return filename_no_extension + "_ascii.txt"


def convert_pixel_to_ascii(pixel: tuple) -> chr:
    brightness = sum(pixel) / 3

    return " .:-=+*#%@"[round(9 * (brightness / 255))]


def asciify_image(args):
    image = Image.open(args.filename)

    # Resize image if necessary
    if args.ratio != 1:
        image = image.resize(
            (int(image.width * float(args.ratio)), int(image.height * float(args.ratio))))

    if args.width != None:
        image = image.resize((int(args.width), int(
            args.height)), resample=Image.LANCZOS)

    image_array = image.load()
    ascii_array = [['c' for _ in range(image.width)]
                   for _ in range(image.height)]

    for i in range(image.width):
        for j in range(image.height):

            char = convert_pixel_to_ascii(image_array[i, j])
            ascii_array[j][i] = char

    return ascii_array


def dump_image(ascii_array, args):
    output = open(args.new_filename, "w")
    for row in ascii_array:
        for pixel in row:
            output.write(pixel)
            if args.gaps == True:
                output.write(" ")
        output.write("\n")
    output.close()


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    validate_args(args)
    if args.new_filename == None:
        args.new_filename = create_new_filename(args.filename)
    if args.ratio == None:
        args.ratio = 1
    ascii_array = asciify_image(args)
    dump_image(ascii_array, args)
