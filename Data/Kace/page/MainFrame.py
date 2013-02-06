'''
Created on Jan 16, 2013

@author: jester
'''
from Lib.Common.ipage import ipage,ilink,iinput,itab


class MainFrame(ipage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    # tabs ono 
    Home_tab=itab("")
    Library_tab=itab("")
    Deployments_tab=itab("")
    Systems_tab=itab("")
    Reports_tab=itab("")
    Settings_tab=itab("")
    
    #links
    Logout_link=ilink("")    
    help_link=ilink("") 
    
    
    #input field
    Search_field=iinput("") 