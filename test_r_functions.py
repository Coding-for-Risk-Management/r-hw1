
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from r_wrapper import RFunctions
import pytest

def test_bond_effective_sensitivity():
    y = 0.03
    face = 2000000
    coupon_rate = 0.04
    m = 10
    ppy = 1
    
    result = RFunctions.get_bpv(y, face, coupon_rate, m, ppy)
    assert round(result) == -1792

def test_arrays1():
    vec = [[1, 2, 3]]
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    result = RFunctions.my_mat_mult(vec, mat)
    assert result[0] == 30
    assert result[1] == 36
    assert result[2] == 42

def test_conditioning():
    result = RFunctions.fizz_buzz(40, 45)
    assert result[0] == "buzz"
    assert result[1] == "41"
    assert result[5] == "fizzbuzz"