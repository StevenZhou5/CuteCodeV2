import pytest
import tensorflow as tf

from deepctr.models import DCN,DeepFM,NFM

from ..utils import get_test_data, SAMPLE_SIZE, check_model


@pytest.mark.parametrize(
    'cross_num, hidden_size, sparse_feature_num, cross_parameterization',
    [(1, (8,), 2, 'vector')]
)
def test_DCN(cross_num, hidden_size, sparse_feature_num, cross_parameterization):
    model_name = "DCN"

    sample_size = SAMPLE_SIZE
    x, y, feature_columns = get_test_data(sample_size,
                                          sparse_feature_num=sparse_feature_num,
                                          dense_feature_num=sparse_feature_num)
    model = DCN(feature_columns,
                feature_columns,
                cross_num=cross_num,
                cross_parameterization=cross_parameterization,
                dnn_hidden_units=hidden_size,
                dnn_dropout=0.5
                )
    check_model(model, model_name, x, y)
