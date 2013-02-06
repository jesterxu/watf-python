'''
Created on Dec 30, 2012

@author: jester
'''
# include all the libraries will be used 
import datetime
from Lib.Common.ifile import *
import WATF_engine

isplitor="="

class ilog(object):
    '''
    this file will handle all the log relates affairs.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        #self.iloger=open(logname,"w")
        
    def openlog(self,logname):
        if os.path.isfile(logname):
            return open(logname,"w")
            
    def closelog(self):
        self.writelog("******************************************************************************\n")
        self.iloger.write(self.timenow()+"\n")
        self.iloger.close()
        
    def writelog(self,itext):
        #self.iloger.write(self.timenow()+"\n")
        itext=str(itext)
        self.iloger.write(itext+"\n")
        
    def writelogheader(self,filename):
        logname="log.txt"
        basepath=os.getcwd()
        
        fp_setup=get_file_as_list(os.path.join(basepath,filename))
        
        itester=WATF_engine.get_value_from_list(fp_setup, "Tester", isplitor)
        iproduct=WATF_engine.get_value_from_list(fp_setup, "Product", isplitor)
        iverison=WATF_engine.get_value_from_list(fp_setup, "Version", isplitor)
        
        logfilepath=os.path.join(basepath,"Results",iproduct,iverison)
        logname=os.path.join(logfilepath,logname)

        self.iloger=self.createlogfile(logname)
        
        
        self.iloger.write(self.timenow()+"\n")
        self.writelog("******************************************************************************\n")
        self.writelog("The product to test:  "+iproduct)
        self.writelog("the version of product:  "+iverison)
        self.writelog("The tester do this test:  "+itester)
        self.writelog("\n******************************************************************************\n")
          
    def timenow(self):
        return  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S' )
    
    
    def createlogfile(self,logname):
        ilogname=logname
        for k in range(1,5000):
            if not os.path.exists(ilogname):
                if not os.path.exists(os.path.dirname(ilogname)):
                    os.makedirs(os.path.dirname(ilogname))
                os.mknod(ilogname)
                return open(ilogname,"w")
            else:
                ilogname=os.path.splitext(logname)[0]+str(k)+os.path.splitext(logname)[1]
            