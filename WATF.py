'''
Created on Dec 31, 2012

This is the main entry for the whole WATF. contains the main modules and work flow.

@author: jester
'''

# this part contains all the library will be used.
from Lib.Common.ifile import *
from Lib.Common.ilog import *
from WATF_engine import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

#we can change the project name when the project changed.
from TestSuites.Kace import *
from TestCases.Kace import *

def main():
    
    #initialize some common variables which will be used always.
    ibasepath=os.getcwd()
    isetup="Setup.ini"
    isplitor="=" 
    
    #this part get all the variables from the setup.ini
    setuplist=get_file_as_list(os.path.join(ibasepath,isetup))
    itestsuites=get_value_from_list(setuplist,"testsuites",isplitor).split(",")
    ihub=get_value_from_list(setuplist,"hub",isplitor)
    iNavigator=get_value_from_list(setuplist,"Navigator",isplitor)


    #initialize the log object here.
    mlog=ilog()
    
    #initialize the navigator.
    if iNavigator.upper()=="IE":
        iNavigator=DesiredCapabilities.INTERNETEXPLORER
    elif iNavigator.upper()=="CHROME":
        iNavigator=DesiredCapabilities.CHROME
    elif iNavigator.upper=="FIREFOX":
        iNavigator=DesiredCapabilities.FIREFOX
    
    #Create the log file and write the head information to the log file.
    mlog.writelogheader(isetup)    
    
    #this part get all the test cases list.
    
    #initialize the test cases array first
    itestcases=[]
    
    for testsuite in itestsuites:
        itestcases=itestcases+eval(testsuite).get_all_testcases()

    
    #this part execute test cases one by one.
    for i in range(1,5000):
        print str(i)+"\n"
        #initialize the array to contain the failed test cases.
        ifailedtestcases=[]
    
        for testcase in itestcases:
            mlog.writelog("we are running the test case: "+ str(testcase)+"\n###################################################################\n")
            print testcase       
            try: 
                driver=webdriver.Remote(ihub,iNavigator)
                mlog.writelog("setup")
                eval(testcase).setup(mlog,driver)
                mlog.writelog("test")
                eval(testcase).test(mlog,driver)
                mlog.writelog("teardown")
                eval(testcase).teardown(mlog,driver)
                driver.quit()
            except Exception as e:
                ifailedtestcases.append(testcase)
                mlog.writelog(e)
                mlog.writelog("exception exists in the " + str(testcase)+" please check it again!")
            finally:
                mlog.writelog("\n\nThe test case "+str(testcase)+" execution finished!\n")
        mlog.writelog("******************************************************************************")
        
    
        #this part will execute the failed test cases second time to ensure this case real failed.
        mlog.writelog("               Re-run the failed test cases.")
        mlog.writelog("******************************************************************************\n\n")
        for testcase in ifailedtestcases:
            mlog.writelog("we are re-running the test case: "+ str(testcase)+"\n###################################################################\n")
            print "**********************************************************************************************"
            print "re-run :"+testcase
            try: 
                driver=webdriver.Remote(ihub,iNavigator)
                mlog.writelog("setup")
                eval(testcase).setup(mlog,driver)
                mlog.writelog("test")
                eval(testcase).test(mlog,driver)
                mlog.writelog("teardown")
                eval(testcase).teardown(mlog,driver)
                driver.quit()
            except Exception as e:
                mlog.writelog(e)
                mlog.writelog("\nException exists in the " + str(testcase)+" please check it again!")
            finally:
                mlog.writelog("\n\nThe test case "+str(testcase)+" execution finished!\n")
    

    #this part handle the log/report.
    mlog.writelog("******************************************************************************")
    mlog.writelog( "All the test cases finished! Please check the report.")
    
    
    #close the log object.
    mlog.closelog()
    
    print "All the test cases finished! Please check the report."
    
    
    
if __name__=="__main__":
    main()