import pytest
from compare import Compare
def test1():
    ver1,ver2 = "1.0","1.1"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.0 is smaller than 1.1")

def test2():
    ver1,ver2 = "1.1","1.0"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.1 is greater than 1.0")

def test3():
    ver1,ver2 = "1.2.0.0","1.2.0"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.2.0.0 is equal to 1.2.0")

def test4():
    ver1,ver2 = "1.2.0","1.2.0.0"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.2.0 is equal to 1.2.0.0")

def test5():
    ver1,ver2 = "1.20","1.2"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.20 is equal to 1.2")

def test6():
    ver1,ver2 = "1.2","1.20"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.2 is equal to 1.20")

def test7():
    ver1,ver2 = "1.13.4.2","1.13.15.2"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.13.4.2 is smaller than 1.13.15.2")

def test8():
    ver1,ver2 ="1.13.15.2", "1.13.4.2"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.13.15.2 is greater than 1.13.4.2")
    
def test9():
    ver1,ver2 ="1.123443.1", "1.1111111.2"
    obj = Compare(ver1,ver2)
    res =obj.compare()
    assert(res =="1.123443.1 is smaller than 1.1111111.2")

