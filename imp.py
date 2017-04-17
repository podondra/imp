#!/usr/bin/env python3.6

import imp.io
import imp.operation
import time


start = time.time()

img = imp.io.read('samples/vychazka.png')
tmp_img = imp.operation.gaussian_blur(img)
imp.io.write(tmp_img, 'samples/output.png')

print(time.time() - start)
