#!/usr/bin/env python3.6

import imp.io
import imp.operation
import time
import argparse


parser = argparse.ArgumentParser(description='A simple image processing tool.')
group = parser.add_mutually_exclusive_group()
group.add_argument('--fliplr', help='flip horizontally', action='store_true')
group.add_argument('--flipud', help='flip vertically', action='store_true')
group.add_argument('--inverse', help='invert colors', action='store_true')
group.add_argument('--rgb2gray', help='convert RGB to grayscale', action='store_true')
group.add_argument('--bright', help='change brightness BRIGHTNESS is float in [-1, 1]', type=float)
group.add_argument('--sharpen', help='sharpen', action='store_true')
group.add_argument('--edge_detection', help='detect edges', action='store_true')
group.add_argument('--box_blur', help='apply box blur', action='store_true')
group.add_argument('--gaussian_blur', help='apply gaussian blur', action='store_true')
parser.add_argument('INPUT', help='input image')
parser.add_argument('OUTPUT', help='output image')
args = parser.parse_args()

# start measure time
start = time.time()

# read input image
img = imp.io.read(args.INPUT)

if args.fliplr:
    img = imp.operation.fliplr(img)
elif args.flipud:
    img = imp.operation.flipud(img)
elif args.inverse:
    img = imp.operation.inverse(img)
elif args.rgb2gray:
    img = imp.operation.rgb2gray(img)
elif args.bright:
    img = imp.operation.brightness(img, args.brightness)
elif args.sharpen:
    img = imp.operation.sharpen(img)
elif args.edge_detection:
    img = imp.operation.edge_detection(img)
elif args.box_blur:
    img = imp.operation.box_blur(img)
elif args.gaussian_blur:
    img = imp.operation.gaussian_blur(img)

# read output image
imp.io.write(img, args.OUTPUT)

# print elapsed time
print('Time:', time.time() - start)
