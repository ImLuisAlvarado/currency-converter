from robux_converter import convertidor_robux
import pytest

def test_convertidor_robux():
    assert convertidor_robux(100) == 5.0