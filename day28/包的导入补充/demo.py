"""
@File : demo.py

@Author: sivan Wu

@Date : 2020/6/14 8:09 上午

@Desc :

"""
import glance  # 可以导入，原因：因为glance与我们这个文件在同一级目录下
print(glance)
# 能不能到某一个包进来就看sys.path就行，如果glance的父目录在sys.path里面就可以导入
import sys
print(sys.path)
# 报错：AttributeError: module 'glance' has no attribute 'api'
# 原因：导入一个包import glance只是相当于执行了这个包下的__init__.py文件，并不是把这个包下的所有文件都导入进来了
# glance.api.policy.get()

# 要想直接导入某个包(文件夹)下的文件
# 方式一： import
import glance.api.policy as policy
policy.get()

# 方式二：from . import .  不可以写成from glance import api.policy ，因为import后面必须是一个明确的文件或方法，
# from import中import后面不能带点，并且from 到 import之间的语句中.号前面必须是一个包
from glance.api import policy  # 直接从一个包中导入文件
from glance.api.policy import get  # 直接从包的文件中导入函数名/变量名
# from glance import api.policy  # 报错
policy.get()


# 进阶：我们就想导入glance之后可以使用glance下的所有文件
# 注意: sys.path中的第一个元素一定是当前执行文件的父目录
import sys
print(sys.path)
# 绝对导入
import glance


# 相对导入 . 表示当前目录，..表示上一级目录
# 因为当我们挪动目录的时候会报错，所以可以使用相对导入，
# 相对导入特点：只要能找到包，就能找到包里的所有文件。
# 相对导入缺点：当我们一个py文件中有相对导入的时候，如果执行该文件就会报错。因为相对导入的文件不可以直接执行



