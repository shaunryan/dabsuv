from dabsuv.taxi import _get_taxis, _get_spark

# duumy test
def test_main():
    taxis = _get_taxis(_get_spark())
    assert taxis.count() > 5
