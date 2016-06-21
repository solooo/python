#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
pillow test
'''
__author__ = 'Eric Pei'

from PIL import Image
im = Image.open('D:/b.jpg')
print (im.format, im.size, im.mode)
im.thumbnail((100,100))
im.save('D:/b1.jpg', 'JPEG')
