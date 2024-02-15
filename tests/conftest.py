import pytest
from app import app

# We'll also create a fixture for the client we'll use to make test requests.
@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client

# Now, when we create a test, if we allow it to accept a parameter called
# `web_client`, Pytest will automatically pass in the web client object.

# For example:

# def test_something(web_client):
#     # web_client is now available to us in this test
