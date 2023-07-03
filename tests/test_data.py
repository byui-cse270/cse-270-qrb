import pytest
import requests

def test_data_endpoint():
    # Make the HTTP GET request
    response = requests.get('http://127.0.0.1:8000/data/all')

    # Verify the response status code
    assert response.status_code == 200

    # Verify the response content
    data = response.json()
    assert isinstance(data, dict)
    assert 'businesses' in data
    businesses = data['businesses']
    assert isinstance(businesses, list)
    assert len(businesses) > 0
    first_business = businesses[0]
    assert isinstance(first_business, dict)
    assert 'name' in first_business
    assert first_business['name'] == 'Teton Elementary'
    # Add additional assertions as needed based on the expected response