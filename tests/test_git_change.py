"""

这个是测试内容变化后。自动重启脚本
"""
import time
from tests.pac1.m1 import show


while 1:
    time.sleep(5)
    show(73)   # 改变这个值，然后推送到git，代码可以自动重启打印新的值。
