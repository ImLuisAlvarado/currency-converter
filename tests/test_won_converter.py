from won_converter import mxn_to_krw
import pytest

def test_mxn_to_krw():
    res_defecto = mxn_to_krw(100)
    assert res_defecto == 7900.0

  

