# -*- coding: utf-8 -*-

'''
enum test
'''

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb'))

print(Month.Jan.name)
print(type(Month))
