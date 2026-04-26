import pytest


# Define the fixture
@pytest.fixture
def sample_data():
    return {"id": 1, "name": "Test Item"}


# Use the fixture in a test
def test_data_integrity(sample_data):
    assert sample_data["id"] == 1
    assert sample_data["name"] == "Test Item"
