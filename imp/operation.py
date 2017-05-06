import numpy as np
from functools import partial


class BrightnessOutOfRangeException(Exception):
    pass

fliplr = np.fliplr

flipud = np.flipud

def inverse(img):
    return 255 - img

def rgb2gray(img):
    # https://www.mathworks.com/help/matlab/ref/rgb2gray.html
    return np.sum(np.array([0.2989, 0.5870,  .1140]) * img, axis=2)

def brightness(img, factor):
    if factor < -1 or 1 < factor:
        raise BrightnessOutOfRangeException

    out_img = img + (255 * factor)

    if factor < 0:
        out_img[out_img < 0] = 0
    else:
        out_img[out_img > 255] = 255

    return out_img

def convolution(img, kernel, factor=1):
    kernel = np.array(kernel, dtype=np.float64).reshape(3, 3, 1)

    out_img = (
            kernel[0][0] * img[:-2, :-2] +
            kernel[0][1] * img[:-2, 1:-1] +
            kernel[0][2] * img[:-2, 2:] +
            kernel[1][0] * img[1:-1, :-2] +
            kernel[1][1] * img[1:-1, 1:-1] +
            kernel[1][2] * img[1:-1, 2:] +
            kernel[2][0] * img[2:, :-2] +
            kernel[2][1] * img[2:, 1:-1] +
            kernel[2][2] * img[2:, 2:]
            )

    out_img *= factor
    out_img[out_img > 255] = 255
    out_img[out_img < 0] = 0
    return out_img

sharpen = partial(convolution, kernel=[
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
    ])

edge_detection = partial(convolution, kernel=[
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
    ])

box_blur = partial(convolution, kernel=[
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
    ], factor=(1 / 9))

gaussian_blur = partial(convolution, kernel=[
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
    ], factor=(1 / 16))
