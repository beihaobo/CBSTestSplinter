import unittest, random, sys
from time import sleep
sys.path.append("..")
from Util.Base_Page import BasePage


# 页面对象（PO) 登录页面
class LoginPage(BasePage):
    url = '/'
    login_username_text_loc ="//*[@id='login-box-inner']/form/div[1]/input"
    login_password_text_loc = "Password"
    login_button_loc = "//*[@id='login-box-inner']/form/div[4]/div/img"
    login_error_hint="//*[@id='login-box-inner']/form/div[3]/div/span"
    login_success_info="/#/Index/"


    def login_username(self,text):
        self.find_by_xpath_first(self.login_username_text_loc).fill(text)

    def login_password(self,text):
        self.find_by_name(self.login_password_text_loc).fill(text)

    def login_button(self):
        self.find_by_xpath_first(self.login_button_loc).click()

    def login_error(self):
        return self.find_by_xpath_first(self.login_error_hint).text

    def login_success(self):
       return self.browser.url.find(self.login_success_info)!="-1"

    def login_action(self,username,password):
        self.login_username(username)
        self.login_password(password)
        self.login_button()
