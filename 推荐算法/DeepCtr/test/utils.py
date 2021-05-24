from __future__ import absolute_import, division, print_function

import inspect
import os
import sys

import numpy as np
import tensorflow as tf
from numpy.testing import assert_allclose
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.layers import Input, Masking
from tensorflow.python.keras.models import Model, load_model, save_model

from deepctr.feature_column import SparseFeat, VarLenSparseFeat, DenseFeat, DEFAULT_GROUP_NAME
from deepctr.layers import custom_objects

SAMPLE_SIZE = 8
VOCABULARY_SIZE = 4
Estimator_TEST_TF1 = True


def gen_sequence(dim, max_len, sample_size):
    return np.array([np.random.randint(0, dim, max_len) for _ in range(sample_size)]), np.random.randint(1, max_len + 1,
                                                                                                         sample_size)

def get_test_data(sample_size=1000, embedding_size=4, sparse_feature_num=1, dense_feature_num=1,
                  sequence_feature=['sum', 'mean', 'max', 'weight'], classification=True, include_length=False,
                  hash_flag=False, prefix='', use_group=False):
    feature_columns = []
    model_input = {}

    if 'weight' in sequence_feature:
        feature_columns.append(
            VarLenSparseFeat(SparseFeat(prefix + "weighted_seq", vocabulary_size=2, embedding_dim=embedding_size),
                             maxlen=3, length_name=prefix + "weighted_seq" + "_seq_length",
                             weight_name=prefix + "weight"))
        s_input, s_len_input = gen_sequence(
            2, 3, sample_size)

        model_input[prefix + "weighted_seq"] = s_input
        model_input[prefix + 'weight'] = np.random.randn(sample_size, 3, 1)
        model_input[prefix + "weighted_seq" + "_seq_length"] = s_len_input
        sequence_feature.pop(sequence_feature.index('weight'))

    for i in range(sparse_feature_num):
        if use_group:
            group_name = str(i % 3)
        else:
            group_name = DEFAULT_GROUP_NAME
        dim = np.random.randint(1, 10)
        feature_columns.append(
            SparseFeat(prefix + 'sparse_feature_' + str(i), dim, embedding_size, use_hash=hash_flag, dtype=tf.int32,
                       group_name=group_name))

    for i in range(dense_feature_num):
        transform_fn = lambda x: (x - 0.0) / 1.0
        feature_columns.append(
            DenseFeat(
                prefix + 'dense_feature_' + str(i),
                1,
                dtype=tf.float32,
                transform_fn=transform_fn
            )
        )
    for i, mode in enumerate(sequence_feature):
        dim = np.random.randint(1, 10)
        maxlen = np.random.randint(1, 10)
        feature_columns.append(
            VarLenSparseFeat(SparseFeat(prefix + 'sequence_' + mode, vocabulary_size=dim, embedding_dim=embedding_size),
                             maxlen=maxlen, combiner=mode))

    for fc in feature_columns:
        if isinstance(fc, SparseFeat):
            model_input[fc.name] = np.random.randint(0, fc.vocabulary_size, sample_size)
        elif isinstance(fc, DenseFeat):
            model_input[fc.name] = np.random.random(sample_size)
        else:
            s_input, s_len_input = gen_sequence(
                fc.vocabulary_size, fc.maxlen, sample_size)
            model_input[fc.name] = s_input
            if include_length:
                fc.length_name = prefix + "sequence_" + str(i) + '_seq_length'
                model_input[prefix + "sequence_" + str(i) + '_seq_length'] = s_len_input

    if classification:
        y = np.random.randint(0, 2, sample_size)
    else:
        y = np.random.random(sample_size)

    return model_input, y, feature_columns


def check_model(model, model_name, x, y, check_model_io=True):
    """
    编译，训练和评测模型，然后存储/加载模型文件
    """
    model.compile('adam', 'binary_crossentropy', metrics=['binary_crossentropy'])
    model.fit(x, y, batch_size=100, epochs=1, validation_split=0.5)
    print(model_name + " 测试和训练通过")
    model.save_weights(model_name + '_weights.h5')
    model.load_weights(model_name + '_weights.h5')
    os.remove(model_name, +'_weights.h5')
    print(model_name + "存储和加载权重测试通过")

    if check_model_io:
        save_model(model, model_name + '.h5')
        model = load_model(model_name + '.h5', custom_objects)
        os.remove(model_name + '.h5')
        print(model_name + "存储和加载模型测试通过")
    print(model_name + "测试通过")


if __name__ == '__main__':
    get_test_data(SAMPLE_SIZE, sparse_feature_num=2, dense_feature_num=2)
