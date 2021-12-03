from day_01 import data_getter


data = data_getter('rsc/test_01_data.txt')

def test_data_getter_gets_all():
    assert len(data) == 3


def test_data_getter_casts_to_ints():
    assert isinstance(data[0], int)


def test_data_getter_maintains_order():
    assert data[1] == 2