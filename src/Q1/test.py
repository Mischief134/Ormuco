import pytest
from q1 import checkOverlap
def test1():
    x1,x2,x3,x4 = 1,4,2,6
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==True)

def test2():
    x1,x2,x3,x4 = 1,4,5,11
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==False)

def test3():
    x1,x2,x3,x4 = -1,-4,-2,-6
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==True)

def test4():
    x1,x2,x3,x4 = -1,-5,-6,-11
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==False)

def test5():
    x1,x2,x3,x4 = -1,2,0,-2
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==True)

def test6():
    x1,x2,x3,x4 = -1,-3,1,3
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==False)

def test7():
    x1,x2,x3,x4 = 0,0,0,0
    res = checkOverlap(x1,x2,x3,x4)
    assert(res ==True)


