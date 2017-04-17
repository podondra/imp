import numpy as np
from functools import partial


fliplf = np.fliplr

flipud = np.flipud

def inverse(img):
    return 255 - img

def rgb2gray(img):
    # https://www.mathworks.com/help/matlab/ref/rgb2gray.html
    out_img = np.zeros_like(img)
    out_shape = (*img.shape[:2], 1)
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    out_img[...] = (0.2989 * r + 0.5870 * g + 0.1140 * b).reshape(out_shape)
    return out_img

def brightness(img, factor):
    if -1 > factor > 1:
        raise Exception
    out_img = np.zeros_like(img)
    out_img = img + (255 * factor)
    if factor < 0:
        out_img[out_img < 0] = 0
    else:
        out_img[out_img > 255] = 255
    return out_img

def convolution(img, kernel, factor=1):
    out_img = np.zeros_like(img)
    kernel = np.array(kernel, dtype=np.float32).reshape(3, 3, 1)
    h, w, _ = img.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            window = img[i - 1:i + 2, j - 1:j + 2]
            out_img[i, j] = np.sum((window * kernel).reshape(-1, 3), axis=0)
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
