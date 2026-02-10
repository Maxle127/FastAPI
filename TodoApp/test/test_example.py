import pytest


def test_equel_or_not_equel():
    assert 3 == 3

class Student():
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years




@pytest.fixture 
def default_employee():
    return Student('Veronika', 'Grinda', 'Computer Science', 2)



def test_person_initialization(default_employee):
    assert default_employee.first_name == 'Veronika', 'First name should be Veronika'
    assert default_employee.last_name == 'Grinda', 'Last name should be Grinda'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 2