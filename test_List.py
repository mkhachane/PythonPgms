import pytest

Mylist = [ ]

@pytest.fixture()
def Insert(x,y,z):
    for i in range(3):
        d = {}
        d['id'] = x
        d['name'] = y
        d['address'] = z
        Mylist.append(d)
    return True

@pytest.fixture()
def Search(m):
    item = m
    for i in Mylist:
        if i['id'] == item:
            return i

@pytest.fixture()
def Remove(a):
    Id = a
    for i in Mylist:
        if i['id'] == Id:
            Mylist.remove(i)
            return True

@pytest.mark.parametrize("x,y,z,expected",[
    (1,'Jon','Kunal Icon',True),
    (2,'Rick','Rose Villa',True),
    (3,'Harry','Nath Villa',True),
])

def test_Insert(x,y,z,expected,Insert):
    assert Insert == expected

@pytest.mark.parametrize("m,expected",[
    (1,{'id':1,'name':'Jon','address':'Kunal Icon'}),
])
def test_Search(m,expected,Search):
    assert Search == expected

@pytest.mark.parametrize("a,expected",[
    (1,True),
])
def test_Remove(a,expected,Remove):
    assert Remove == expected
