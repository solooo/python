#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code


    def info(self):
        print('name: %s, code: %s' %(self._name, self._code))
        
if __name__ == '__main__':
    s = Student()
    s.name = 'eric'
    s.code = '001'
    s.info()
    #print(s.__name)
