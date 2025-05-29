import pytest

@pytest.fixture
def sample_use():
    return{
        "name": "Nico",
        "email": "nico@example.com",
        "age": 36
    }

@pytest.fixture
def sample_number_list():
    return [1, 2, 3,4,5]
