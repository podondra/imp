import numpy as np


fliplf = np.fliplr

flipud = np.flipud

def inverse(img):
    return 255 - img

def rgb2gray(img):
    # https://www.mathworks.com/help/matlab/ref/rgb2gray.html
    gray_img = np.zeros_like(img)
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    gray = (0.2989 * r + 0.5870 * g + 0.1140 * b)
    gray_img[...] = gray.reshape(*gray.shape, 1)
    return gray_img

def brightness(img, factor):
    if -1 > factor > 1:
        raise Exception
    new_img = img.astype(np.int)
    new_img = new_img + int(round(255 * factor))
    if factor < 0:
        new_img[new_img < 0] = 0
    else:
        new_img[new_img > 255] = 255
    return new_img.astype(np.uint8, copy=False)
