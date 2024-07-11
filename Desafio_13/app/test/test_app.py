import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_hello_world(client):
    """Test Hola a Todos"""
    rv = client.get('/')
    assert rv.data == b'Hola a Todos, Esto anda sorprendentemente!'
