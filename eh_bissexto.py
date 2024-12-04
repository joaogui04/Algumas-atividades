import pytest
def eh_bissexto(ano:int)->bool:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else: 
        return False


def test_01():

    assert eh_bissexto(2000) == True

def test_02():

    assert eh_bissexto(1600) == True


def test_03():

    assert eh_bissexto(1800) == False

def test_04():

    assert eh_bissexto(0) == True

def test_05():

    assert eh_bissexto(1) == False

def test_06():

    assert eh_bissexto(9999) == False


def test_07():

    assert eh_bissexto(4) == True