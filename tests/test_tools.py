from toolbox.tools import hello_world
from toolbox.tools import doubler

def test_length_of_hello_world():
    assert len(hello_world()) != 0

def test_type_doubler():
    assert type(doubler(7)) == int
