import pytest
from app import app

@pytest.fixture
def client():
    # Konfigurasi aplikasi untuk testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    # Test route utama ('/')
    response = client.get('/')
    
    # Cek status code 200 (OK)
    assert response.status_code == 200
    
    # Cek konten response
    assert b"Hello DevOps World!" in response.data

def test_invalid_route(client):
    # Test route yang tidak ada
    response = client.get('/invalid-route')
    
    # Cek status code 404 (Not Found)
    assert response.status_code == 404