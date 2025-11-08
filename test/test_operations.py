import numpy as np
import pytest
from scic import add, divide, mean

def test_add():
    np.testing.assert_array_equal(add([1,2],[3,4]), np.array([4,6]))

def test_mean():
    assert mean([1,2,3]) == pytest.approx(2.0)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide([1,2],[1,0])
