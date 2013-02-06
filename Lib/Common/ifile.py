'''
Created on Dec 30, 2012

@author: jester
'''
import os

def get_file_as_list(filename):
    if os.path.isfile(filename):
        fp=open(filename,'r')
        return fp.readlines() 
        fp.close()
    else:
        print "the input wat not an file, please check again."