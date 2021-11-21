from src.ortools_examples.mip_hello_world import mip_hello_world


def test_mip_hello_world():
    assert {25, 0, 0} == mip_hello_world()
