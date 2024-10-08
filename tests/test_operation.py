from src.math_operation import add, sub

def test_add():
    assert add(2,3)==5 # checks  if the function add returns 5 when given 2 and 3 as arguments
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub (4,1)==3
    assert sub (4,2)==2
