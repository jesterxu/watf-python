def setup(mlog,driver):
    mlog.writelog("setup")
    
    
def test(mlog,driver):
    mlog.writelog("test") 
    
def teardown(mlog,driver):
    mlog.writelog("teardown")