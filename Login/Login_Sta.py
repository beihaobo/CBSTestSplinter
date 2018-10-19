from time import sleep
import unittest, random, sys
sys.path.append("..")
from Util.Base_Case import BaseCase
from Util.Core import htmlTestRunner
from Login_Page import LoginPage


class loginTest(BaseCase):
    '''社区登录测试'''
    waitback=1

    def test_login_user_pawd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.browser)
        po.open()
        po.login_action("","")
        sleep(self.waitback)
        self.assertEqual(po.login_error(),'请输入帐号')

    def test_login_pawd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.browser)
        po.open()
        po.login_action("testaaa","")
        sleep(self.waitback)
        self.assertEqual(po.login_error(), '请输入密码')

    def test_login_user_pawd_error(self):
        '''用户名、密码为错误'''
        po = LoginPage(self.browser)
        po.open()
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "test" + character
        po.login_action(username,"@#$%")
        sleep(self.waitback)
        self.assertEqual(po.login_error(), '用户名或密码错误')

    def test_login_success(self):
        '''用户名、密码正确，登录成功'''
        po = LoginPage(self.browser)
        po.open()
        po.login_action("simple","111111")
        sleep(self.waitback)
        #po2 = MailPage(self.browser)
        self.assertTrue(po.login_success())


if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(loginTest("test_login_user_pawd_null"))
    suit.addTest(loginTest("test_login_pawd_null"))
    suit.addTest(loginTest("test_login_user_pawd_error"))
    suit.addTest(loginTest("test_login_success"))
    htmlTestRunner(htmlTestRunner,suit)
