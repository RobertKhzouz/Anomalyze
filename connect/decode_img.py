import base64

from time import localtime, strftime

def decode(img_string):
    img_data = base64.b64decode(img_string)

    file_name = f'{strftime('%Y_%m_%d_%H_%M_%S', localtime())}.jpg'

    with open(file_name, 'wb') as img:
        img.write(img_data)

    print('Image saved!')