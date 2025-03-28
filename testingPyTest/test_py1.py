import pytest
pytestmark = [pytest.mark.smokee]

@pytest.mark.sanity
def test_a1():
    assert 5==5

def test_a2():
        assert 5-5==0,"failed intentlny"

@pytest.mark.parametrize("input",[12,34,67])
def test_a3(input):
    print(input,end="--")

@pytest.fixture()
def set_fix():
    print("in fixture")
    list1=[12,34,55]
    return list1

def test_a4(set_fix):

    print(set_fix)
    assert 1

