#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单元测试
# 编写功能代码；编写测试用例代码；如果测试用例代码通过说明功能代码ok，否则功能代码有问题；
# 当功能代码修改时，重新跑测试用例代码，如果不通过要么是功能代码有问题，要么需要修改测试用例代码
# 现在我们编写一个Dict类，这个类和dict一致，但是可以通过属性来访问
class Dict(dict):
    '''
    文档注释：https://www.liaoxuefeng.com/wiki/1016959663602400/1017605739507840
    下面的代码doctest会自动执行测试: 如果全部执行通过则不会输入异常，否侧会输入异常log，注意不能在输出结果后加注释
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x # 如果下一行改为1000将会测试不通过
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1,b=2,c='3')
    >>> d2.c
    '3'
    >>> d2['empty'] # 如果输出的太多，可以值输出头尾信息
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict'中没有属性：empty
    '''

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):  # 当找不到对应方法和属性时就会走到这个方法
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict'中没有属性：%s" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 下面我们就要编写单元测试来验证我们的Dict类是否正确
# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

if __name__ == '__main__':
    # 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
    # 所以，不必担心doctest会在非测试环境下执行。
    import doctest  # 引入文档测试模块
    doctest.testmod()
