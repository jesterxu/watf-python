'''
Created on Dec 30, 2012

Description: this module contains all the important functions will used in WATF.

@author: jester
'''
#this part import all the lib will needed.
#import os


# this function to get the value from the list item pairs.
def get_value_from_list(ilist,item,isplitor):
    if ilist!=None:
        ifound=False
        for iitem in ilist:
            if iitem.find(item)!=-1:
                ifound=True
                return iitem.split(isplitor)[1].strip()
            
        if not ifound:
            print "the value can't be found from this list:"+ilist
        