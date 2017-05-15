#!/usr/bin/env python3.6

import imp.io
import imp.operation
import time
import argparse


parser = argparse.ArgumentParser(description='A simple image processing tool.')

group = parser.add_mutually_exclusive_group()
group.add_argument(
        '--fliplr',
        help='flip horizontally',
        action='store_true'
        )
group.add_argument(
        '--flipud',
        help='flip vertically',
        action='store_true'
        )
group.add_argument(
        '--transpose',
        help='transpose image',
        action='store_true'
        )
group.add_argument(
        '--rotate',
        help='rotate image left',
        action='store_true'
        )
group.add_argument(
        '--inverse',
        help='invert colors',
        action='store_true'
        )
group.add_argument(
        '--grayscale',
        help='convert to grayscale',
        action='store_true'
        )
group.add_argument(
        '--bright',
        help='change brightness BRIGHTNESS is float in [-1, 1]',
        type=float
        )
group.add_argument(
        '--sharpen',
        help='sharpen',
        action='store_true'
        )
group.add_argument(
        '--edge',
        help='apply kernel which detects edges',
        action='store_true'
        )
group.add_argument(
        '--box',
        help='apply box blur',
        action='store_true'
        )
group.add_argument(
        '--gaussian',
        help='apply gaussian blur',
        action='store_true'
        )

parser.add_argument('INPUT', help='input image')
parser.add_argument('OUTPUT', help='output image')

args = parser.parse_args()

# read input image
img = imp.io.read(args.INPUT)

if args.fliplr:
    img = imp.operation.fliplr(img)
elif args.flipud:
    img = imp.operation.flipud(img)
elif args.inverse:
    img = imp.operation.inverse(img)
elif args.grayscale:
    img = imp.operation.rgb2gray(img)
elif args.bright:
    img = imp.operation.brightness(img, args.bright)
elif args.sharpen:
    img = imp.operation.sharpen(img)
elif args.edge:
    img = imp.operation.edge_detection(img)
elif args.box:
    img = imp.operation.box_blur(img)
elif args.gaussian:
    img = imp.operation.gaussian_blur(img)

# write output image
imp.io.write(img, args.OUTPUT)
