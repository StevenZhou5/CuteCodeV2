import pytest


@pytest.mark.a
def test_fun_a1():
    assert 3 > 5


@pytest.mark.a
def test_fun_a2():
    assert 2 > 1


@pytest.mark.b
def test_fun_b1():
    assert 1 < 2


@pytest.mark.b
def test_fun_b2():
    assert 5 < 8
