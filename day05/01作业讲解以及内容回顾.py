"""
@File : 01作业讲解以及内容回顾.py

@Author: sivan Wu

@Date : 2020/6/16 4:27 下午

@Desc :

"""

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)
print(li)
# li += l2  # 相当于extend，但是不推荐，因为+=也会帮助我们调用list.__add__，所以最后还是会调用函数
# 因为[1, 2, 3] + [4, 5, 6] 其实python会自动帮我们调用list.__add__([4,5,6])
# print(li)
print(li)
li.pop()
print(li)
print(li)
del li[0]
print(li)
print(','.join())