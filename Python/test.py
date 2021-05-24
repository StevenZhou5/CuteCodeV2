class MyTest():
    aa = ["a", "b", "c"]


if __name__ == '__main__':
    dict_a = {}
    dict_a["a"] = MyTest.aa
    print(dict_a["a"])
