#!/usr/bin/env python3.6

import imp.io
import imp.operation


img = imp.io.read('samples/vychazka.png')
tmp_img = imp.operation.brightness(img, 0.1)
imp.io.write(tmp_img, 'samples/output.png')
