#!/usr/bin/env python3
from PIL import Image

LINE_HEIGHT = 28
START_FILENUM = 7
END_FILENUM = 368
DIVIDER_MARGIN = 100
HEADER_WIDTH = 186
FOOTER_WIDTH = 89

"""
Returns True if a black line of height LINE_HEIGHT with
top tip at position x exists and False otherwise.
"""
def line_is_here(image, fixed_x, starting_y):
    for y in range(starting_y, starting_y + LINE_HEIGHT):
        if image.getpixel((fixed_x, y)) != (0, 0, 0):
            return False
    return True

failed_files = []
for filenum in range(START_FILENUM, END_FILENUM + 1):
    # Open the image and get its dimensions
    filename = str(filenum).zfill(3) + '.png'
    im = Image.open(f'dict/{filename}').convert('RGB')
    width, height = im.size
    center_x, center_y = width // 2, height // 2

    # Search for the divider at the center of the image
    divider_location = None
    for w in range(center_x - DIVIDER_MARGIN, center_x + DIVIDER_MARGIN):
        if (line_is_here(im, w, center_y)):
            divider_location = w + 1
            break

    # Crop and save images with detected divider
    if not divider_location:
        failed_files.append(filenum)
    else:
        im_left = im.crop((0, HEADER_WIDTH, divider_location, height - FOOTER_WIDTH))
        im_left.save('dict_cropped/{}'.format(filename.replace('.','a.')))
        im_right = im.crop((divider_location, HEADER_WIDTH, width, height - FOOTER_WIDTH))
        im_right.save('dict_cropped/{}'.format(filename.replace('.','b.')))

if failed_files:
    print('Failed to detect divider for images', *failed_files)
    print('Please crop these images manually.')
