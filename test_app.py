import pytest
import os
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Fichiers disponibles" in response.data

def test_api_files(client):
    response = client.get('/api/files')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_download_file(client):
    filename = "example.txt"
    file_path = os.path.join("Listed&Downloaded_Files", filename)
    # Remplissage du fichier
    with open(file_path, "w") as f:
        f.write("Test file content")
    # Telechargement du fichier
    response = client.get(f'/download/{filename}')
    assert response.status_code == 200
    assert b"Test file content" in response.data
    # File deleted 
    import time
    time.sleep(0.1)  
    os.remove('Listed&Downloaded_Files/example.txt')

