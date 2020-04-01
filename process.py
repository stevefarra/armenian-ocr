#!/usr/bin/env python3
import os, io
from google.cloud import vision
from google.cloud.vision import types

START_PAGE = 7
END_PAGE = 368

# Setup
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service_acc_token.json'
client = vision.ImageAnnotatorClient()

def populate_file_name_list(start_page, end_page):
    file_name_list = []
    for i in range(start_page, end_page + 1):
        page = os.path.abspath('dict_cropped/{}.png'.format(str(i).zfill(3)))
        left_page = page.replace('.','a.')
        right_page = page.replace('.','b.')
        file_name_list.append(left_page)
        file_name_list.append(right_page)
    return file_name_list

def image_to_text(file_name):
    # Load the image
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image, image_context={"language_hints": ["hy", "en"]})
    texts = response.text_annotations

    # Output to file
    with open('out.txt', 'a') as f:
        print(format(texts[0].description),file=f)

file_name_list = populate_file_name_list(START_PAGE, END_PAGE)

for file_name in file_name_list:
    image_to_text(file_name)