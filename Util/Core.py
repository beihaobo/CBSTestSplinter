from splinter import Browser
import os
from HTMLTestRunner import HTMLTestRunner

#启动浏览器驱动
def browser(self,browserName='chrome'):
	return Browser(browserName)

#获取HTMLTestRunner测试驱动
def htmlTestRunner(self,test_suite,file_name="./result.html",_title="数禧金融产品测试报告",_desc="用例执行情况:"):
	fp=open(file_name,'wb')#定义报告存放该路径
	#定义测试报告
	runner=HTMLTestRunner(stream=fp,title=_title,description=_desc)
	#运行测试用例
	runner.run(test_suite)
	#关闭报告文件
	fp.close()

#插入图片#
def shot(browser, module,file_name):
    #base_dir = os.path.dirname(os.path.dirname(__file__))
    
    base_dir = os.getcwd()
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/CBSTestSplinter/')[0]
    file_path =base+ "/CBSTestSplinter/report/" + module+"/image/" + file_name
    #print(file_path)
    browser.driver.save_screenshot(file_path)

#
