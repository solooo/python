# -*- coding:utf-8 -*-
import datetime
import functools

def costing(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = datetime.datetime.now()
        print (start_time)
        func()
        end_time = datetime.datetime.now()
        print (end_time)
        print ("time used: {}".format(end_time - start_time))
    return wrapper

@costing
def loop():
    for i in range(10000):
        pass
    print ('finished.')

if __name__ == "__main__":
    loop()

    
