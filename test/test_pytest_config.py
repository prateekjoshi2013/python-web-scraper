import math

import pytest


def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def testequality():
   assert 10 == 11


def test_greater():
   num = 100
   assert num > 100

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200

#input fixture in conftest.py
def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0


# multiple parameters testing
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output



@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num < 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200
