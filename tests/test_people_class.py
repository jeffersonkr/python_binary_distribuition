import pytest
from app.models.people import People

@pytest.fixture(scope='function')
def new_people():
    jose = People(name='jose', age=44)
    yield jose
    del jose

def test_instance_people_class(capsys):
    andre = People(name='andre', age=25)
    assert isinstance(andre, People)
    print(andre)
    capture = capsys.readouterr().out
    assert 'andre' in  capture

def test_age_property(new_people):
    assert new_people.age == 44

def test_getting_older(new_people):
    assert new_people.age == 44
    new_people.get_older()
    assert new_people.age == 45
    new_people.get_older(2)
    assert new_people.age == 47

def test_people_eating(new_people, capsys):
    new_people.eat()
    capture = capsys.readouterr().out
    assert "jose is eating" in capture