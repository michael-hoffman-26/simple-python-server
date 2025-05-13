import pytest
from main import app

@pytest.fixture
def client():
    """Create a test client for our app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test the /api/hello endpoint."""
    # Make a GET request to the endpoint
    response = client.get('/api/hello')
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response is JSON
    assert response.content_type == 'application/json'
    
    # Check if the response has the expected data
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Hello, World!'

def test_hello_endpoint_method_not_allowed(client):
    """Test that POST request to /api/hello is not allowed."""
    # Make a POST request to the endpoint
    response = client.post('/api/hello')
    
    # Check if the response status code is 405 (Method Not Allowed)
    assert response.status_code == 405 