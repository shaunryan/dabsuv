from manisha.taxi import get_taxis

def test_main():
    taxis = get_taxis(_get_spark())
    assert taxis.count() == 5
