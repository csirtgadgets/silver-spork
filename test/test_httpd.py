import json
from pprint import pprint

import pytest
import csirtg_predict_api as httpd

@pytest.fixture
def client(request):
    return httpd.application.test_client()


def test_httpd_help(client):
    rv = client.get('/')
    assert rv.status_code == 200


def test_httpd_ip(client):
    rv = client.get('/ip/?q=127.0.0.1,2')
    assert rv.status_code == 200

    rv = json.loads(rv.data)
    assert rv['data'] == '1'


def test_httpd_domain(client):
    rv = client.get('/domain/?q=google.com')
    assert rv.status_code == 200

    rv = json.loads(rv.data)
    assert rv['data'] == '0'

    rv = client.get('/domain/?q=go0gle.com')
    assert rv.status_code == 200

    rv = json.loads(rv.data)
    assert rv['data'] == '1'


def test_httpd_url(client):
    rv = client.get('/url/?q=http://google.com')
    assert rv.status_code == 200

    rv = json.loads(rv.data)
    assert rv['data'] == '0'

    rv = client.get('/url/?q=http://g0ogle.com')
    assert rv.status_code == 200

    rv = json.loads(rv.data)
    assert rv['data'] == '1'
