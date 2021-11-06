class MyTest():
    aa = ["a", "b", "c"]


from enum import Enum, unique


@unique
class OMG_DATA_PREPROCESSOR(Enum):
    '''
    定义不同处理数据方法的常量枚举
    '''
    # CTR相关模型：1-100
    TYPE_CTR_V0 = 1

    # 互动ugc模型：1001-1100
    TYPE_UGC_BASE = 2
    TYPE_UGC_ONLY_REVIEW = 3.0

    # MMOE多任务相关：1101-1200
    TYPE_MMOE_V0 = "4"


if __name__ == '__main__':
    # dict_a = {}
    # dict_a["a"] = MyTest.aa
    # print(dict_a["a"])
    # print(OMG_DATA_PREPROCESSOR.TYPE_MMOE_V0 == OMG_DATA_PREPROCESSOR.TYPE_CTR_V0)
    # print(type(3.0))
    # print(type(OMG_DATA_PREPROCESSOR.TYPE_UGC_ONLY_REVIEW))
    # print(OMG_DATA_PREPROCESSOR.TYPE_UGC_ONLY_REVIEW == 3.0)
    print(5 >> 1)
    print(5 << 2)
