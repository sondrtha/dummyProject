import utils

def test_multiply_by_three():
    assert(utils.multiply_by_three(5) == 15)
    assert(utils.multiply_by_three(10) == 30)

def test_add5():
    assert(utils.add5(10) == 15)


def test_add_should_fail():
    assert(utils.add5(5) == 15)