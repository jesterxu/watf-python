'''
Created on Jan 16, 2013

@author: jester
'''

class ipage(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
class icontrol(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    ilocator=""

class ilink(icontrol):
    '''
    
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    def setlocator(self,ilocator):
        return ilocator
        
class itab(icontrol):
    '''
    
    '''
    
    def __init__(self,locator):
        '''
        Constructor
        '''
        ilocator=locator
    def setlocator(self,ilocator):
        return ilocator
        
class ibutton(icontrol):
    '''
    
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    def setlocator(self,ilocator):
        return ilocator
        
class iinput(icontrol):
    '''
    
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    def setlocator(self,ilocator):
        return ilocator