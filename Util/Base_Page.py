# 基本层
class BasePage(object):

    def __init__(self,browser,base_url="http://demo.icwn.cn"):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30

    #宽口的打开关闭#
    def _open(self,url):
        url_ = self.base_url + url # = http://www.126.com/index.html
        #print(url_)
        self.browser.visit(url_)
       

    def open(self):
        self._open(self.url)

    def close():
        self.browser.quit()






    #查找界面元素
    def find_by_css(self,loc):
        return self.browser.find_by_css(loc)



    def find_by_xpath(self,loc):
        return self.browser.find_by_xpath(loc)

    def find_by_xpath_first(self,loc):
        return self.browser.find_by_xpath(loc).first

    def find_by_xpath_last(self,loc):
        return self.browser.find_by_xpath(loc).last

    def find_by_xpath_index(self,loc,index):
        return self.browser.find_by_xpath(loc)[index]



    def find_by_tag(self,loc):
        return self.browser.find_by_tag(loc)


    def find_by_name(self,loc):
        return self.browser.find_by_name(loc)

    def find_by_name_first(self,loc):
        return self.browser.find_by_css(loc).first

    def find_by_name_first(self,loc):
        return self.browser.find_by_css(loc).last

    def find_by_name_index(self,loc,index):
        return self.browser.find_by_css(loc)[index]




    def find_by_text(self,*loc):
        return self.browser.find_by_text(loc)

    def find_by_id(self,loc):
        return self.browser.find_by_id(loc)

    def find_by_value(self,loc):
        return self.browser.find_by_value(loc)





    def  find_link_by_text(self,loc):
        return self.browser.find_link_by_text(loc)

    def  find_link_by_partial_text(self,loc):
        return self.browser.find_link_by_partial_text(loc)

    def  find_link_by_href(self,loc):
        return self.browser.find_link_by_href(loc)

    def  find_link_by_partial_href(self,loc):
        return self.browser.find_link_by_partial_href(loc)




    #点击查找界面元素

