# ascii-image-converter
A simple script to convert an image to a 2-D array of ascii characters.
Depends on PIL being installed.

USAGE:
  convert.py [filename] [-n new_filename] [-r ratio] [-w width -h height] [-s]
  "-s" is a boolean flag which prints spaces between each character in a row in an attempt to preserve aspect ratio. You can't specify both ratio and width/height, and if you must specify either width AND height or neither. If a new filename is not specified, the program names the new file for you. 
