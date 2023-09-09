# Importing Required Modules
from rembg import remove
from PIL import Image

import os

files = os.listdir(os.path.dirname(__file__))
images = [file for file in files if file.lower().endswith(('jpg', 'png'))]

def main():
    size = int(input('Size: '));
    for image in images:
        input_path = os.path.join(os.path.dirname(__file__), image)
        print('Processing: ' + input_path)
        output_path = os.path.join(os.path.dirname(__file__), 'test', os.extsep.join([os.path.splitext(image)[0], 'png']))
        print('Saving to: ' + output_path)
        input_image = Image.open(input_path)
        input_image = input_image.resize(size=(size, input_image.height * size // input_image.width))
        out_put_image = remove(input_image)
        out_put_image.save(output_path)
        print('Done!')

main()
