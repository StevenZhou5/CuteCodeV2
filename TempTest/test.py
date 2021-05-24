#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'全局注释：提供py文件测试'

__author__ = 'Steven Zhou'


# ======================<editor-fold des = '利用filter()来生成素数(质数)'> =============
def _odd_iter():  # 质数一定是奇数，所以先定义一个奇数生成器
    n = 1
    while True:
        n += 2
        yield n


# next(_odd_iter())
def _not_divisible(n):
    return lambda x: x % n > 0


def primes_iter():  # 定义一个素数生成器
    yield 2  # 第一个素数是2
    it = _odd_iter()  # 用奇数生成器初始化数据
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n  # 第一次这里会返回三，后面
        #         it = filter(lambda x : x % n > 0, it) # 要保证后面的数除以当前的最新的质数除不尽
        it = filter(_not_divisible(n), it)  # 这里是在构造新的数列：这个数列必须满足后面的数除以前面的数都除不尽才可以，否则就会把next(it)过滤掉


def test_generate_primes():
    g_primes = primes_iter()
    next(g_primes)
    next(g_primes)
    next(g_primes)
    next(g_primes)
    # 第五步
    next(g_primes)
    # for _ in range(5):
    #     print(next(g_primes))


# </editor-fold>


# ============================= <editor-fold des="简单测试"> =============================
import sys


def test_simple_module():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。
    # argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    for i in range(len(args)):
        print('args[', i, ']:', args[i])


# </editor-fold>


# ============================= <editor-fold des="h5文件存储测试"> =============================
import h5py


def save_data(file_name):
    name = '周振武'
    age = 27
    f = h5py.File('/Users/zhenwuzhou/.keras/datasets/' + str(file_name) + '.h5', 'w')  # 注意'w'必须小写
    f.create_dataset('name', data=name)  # 可以使用这种Key——Value形式存储
    f['age'] = age  # 也可以使用这种Key——Value形式存储
    f.close()


def get_data(file_name):
    f = h5py.File('/Users/zhenwuzhou/.keras/datasets/' + str(file_name) + '.h5', 'r')
    print(f['name'][()])
    print(f['age'][()])
    f.close()


def h5_save_test():
    save_data('user_info')
    get_data('user_info')


# </editor-fold>

# ============================= <editor-fold des="h5文件存储测试"> =============================
import logging


def test_logging():
    # a = list(range(10))
    logging.info("sss:")
    print("sss")


# </editor-fold>
# 当我们在命令行运行test.py模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    # test_generate_primes()  # 测试质数生成
    # test_simple_module()
    test_logging()
