from PIL import Image
import numpy as np


def read(fp):
    '''Open image with Pillow lib and return it as numpy array.'''
    return np.asarray(Image.open(fp))

def write(img, fp):
    '''Write array as image to fp.'''
    try:
        Image.fromarray(img).save(fp)
    except (KeyError, IOError) as e:
        print(e)
        return False
    return True
