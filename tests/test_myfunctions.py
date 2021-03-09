from hello import myfunctions

def test_hello():
    assert myfunctions.hello('world') == 'hello, world'
