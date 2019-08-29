import os, json

import pytest

from wct_app.main.app import APP

@pytest.fixture
def client():
    client = APP.test_client()
    APP.config['TESTING'] = True
    yield client

ROUTE = '/api/v0/widgetize'

def test_good_payload(client):
    r = client.post(ROUTE, data=json.dumps({'widget_material': 'foo'}))
    data = r.get_json()
    assert r.status_code == 200
    assert 'wct_version' in data.keys()
    assert 'widget' in data.keys()
    assert '(ಠ_ಠ)' in data.get('widget', '')

def test_bad_payload(client):
    r = client.post(ROUTE, data=json.dumps({'bad_material': 'foo'}))
    assert r.status_code == 400
