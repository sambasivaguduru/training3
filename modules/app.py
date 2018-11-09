"""
import sys
print sys.path
import test1
"""
'''
import folder1
folder1.test3.fun()
'''
from folder1 import test3
test3.fun()