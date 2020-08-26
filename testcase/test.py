import os
import shelve
import time
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# option=Options()
# option.debugger_address ="127.0.0.1:9222"
# driver=webdriver.Chrome(options=option)
# driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
# cookies=driver.get_cookies()
# print(cookies)

# cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850762041417'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ruD4p7_D3V8nP9efyWTYFDtVSbAkex7kVUBLq5cX6TwBJsDW0i3QAk8Iw4-BlcfjI8iIsxsSDA_KWr7S5WM_VG0gAe4wqqm9-vwWS5AqpnDP51P66oi510rXpArwxx89XJVz2BzjhJiCMhEktBIe0IE5vAx4bJ_B4BSFMcpqlf5d5D9QyG6WC_JugKrJvMTKjzA-r5tr5R6oxWpRySmYSe2jr7oynQEc3GRjAMaucDHtnuMjDJpJCLlzws2WJYsOsAy4umCZM_yrEuyJ9UW3Cw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850762041417'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324945154528'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'I2FjK4rO91ceRtQiBo8zabAF6dblFX3OdmFIvE6cchnarMNYYF-Wpf79kFtJMu0U'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4945624'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '29990006922368939'}, {'domain': '.qq.com', 'expiry': 1661499793, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1932096905.1598411760'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629947746, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1599881506, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '454529560@qq.com'}, {'domain': '.qq.com', 'expiry': 1896765615, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1598514193, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.614817006.1598411760'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598443282, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3na4vcn'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1378462720'}, {'domain': '.work.weixin.qq.com', 'expiry': 1601020908, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '35c88d120256b92a71153a30a04a469961852d263d2ea1d4e42ea1a7329d5871'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1411160745'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629948005, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598411759'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4985325315'}, {'domain': '.qq.com', 'expiry': 1864857845, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_1411160745'}, {'domain': '.qq.com', 'expiry': 2147483652, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'ZXIwANR1Wr'}]


# db = shelve.open("../file/cookies")
# db['cookies']=cookies
# db.close()
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#
# db = shelve.open("../file/cookies")
# cookies=db['cookies']
# db.close()
# print(cookies)
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
# time.sleep(10)
# driver.find_element(By.CSS_SELECTOR,'[node-type="addmember"]').click()
filepath = os.path.dirname(__file__)
filename="../file/address.xlsx"
print(filepath)
print(os.path.abspath(os.path.join(filepath,filename)))