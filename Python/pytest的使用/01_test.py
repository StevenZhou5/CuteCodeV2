import pytest


# 方法名必须以test结尾：XXX_test()
# pytest -v 01_test.py显示了更详细的输出。

# 使用skip跳过某个测试
@pytest.mark.skip
def test_fun1():
    val = 1
    assert val == 1

def test_fun2():
    val = 2
    # assert val == 1
    print(val)


@pytest.mark.parametrize(
    'a,b',
    [(3, 5), (7, 8)]
)
def test_fun3(a, b):
    res = a + b
    print(res)


