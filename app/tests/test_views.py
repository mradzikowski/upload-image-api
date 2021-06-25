import json

import pytest

from images.models import Account
from .images.conftest import add_account


@pytest.mark.django_db
def test_add_account(client):
    accounts = Account.objects.all()
    assert len(accounts) == 0
    resp = client.post(
        "/api/account/",
        {
            "name": "Basic"
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data['name'] == "Basic"

    accounts = Account.objects.all()
    assert len(accounts) == 1


@pytest.mark.django_db
def test_add_account_invalid_json(client):
    accounts = Account.objects.all()
    assert len(accounts) == 0

    resp = client.post(
        "/api/account/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400
    accounts = Account.objects.all()
    assert len(accounts) == 0


@pytest.mark.django_db
def test_get_single_account(client, add_account):
    account = add_account(name="Premium")
    resp = client.get(f"/api/account/{account.id}/")
    assert resp.status_code == 200
    assert resp.data['name'] == "Premium"


def test_get_single_account_incorrect_id(client):
    resp = client.get(f"/api/account/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_accounts(client, add_account):
    account_one = add_account(name="Premium")
    account_two = add_account(name="Basic")
    resp = client.get(f"/api/account/")
    assert resp.status_code == 200
    assert resp.data[0]['name'] == account_one.name
    assert resp.data[1]['name'] == account_two.name