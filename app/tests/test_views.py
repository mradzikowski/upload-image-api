import pytest

from images.models import Account, User

from .images.conftest import add_account


@pytest.mark.django_db
def test_add_account(client):
    accounts = Account.objects.all()
    assert len(accounts) == 0
    resp = client.post(
        "/api/account/", {"name": "Basic"}, content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "Basic"

    accounts = Account.objects.all()
    assert len(accounts) == 1


@pytest.mark.django_db
def test_add_account_invalid_json(client):
    accounts = Account.objects.all()
    assert len(accounts) == 0

    resp = client.post("/api/account/", {}, content_type="application/json")
    assert resp.status_code == 400
    accounts = Account.objects.all()
    assert len(accounts) == 0


@pytest.mark.django_db
def test_get_single_account(client, add_account):
    account = add_account(name="Premium")
    resp = client.get(f"/api/account/{account.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Premium"


def test_get_single_account_incorrect_id(client):
    resp = client.get(f"/api/account/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_accounts(client, add_account):
    account_one = add_account(name="Premium")
    account_two = add_account(name="Basic")
    resp = client.get(f"/api/account/")
    assert resp.status_code == 200
    assert resp.data[0]["name"] == account_one.name
    assert resp.data[1]["name"] == account_two.name


@pytest.mark.django_db
def test_remove_account(client, add_account):
    account = add_account(name="Premium")
    resp = client.get(f"/api/account/{account.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Premium"

    resp_two = client.delete(f"/api/account/{account.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get(f"/api/account/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_move_incorrect_id(client):
    resp = client.delete(f"api/account/1000/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_account(client, add_account):
    account = add_account(name="Basic")
    resp = client.put(
        f"/api/account/{account.id}/",
        {"name": "Premium"},
        content_type="application/json",
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "Premium"

    resp_two = client.get(f"/api/account/{account.id}/")
    assert resp_two.status_code == 200
    assert resp_two.data["name"] == "Premium"


@pytest.mark.django_db
def test_update_account_incorrect_id(client):
    resp = client.put(f"api/account/1000/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_account_invalid_json(client, add_account):
    account = add_account(name="Premium")
    resp = client.put(
        f"/api/account/{account.id}/", {}, content_type="application/json"
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_update_account_invalid_json_keys(client, add_account):
    account = add_account(name="Premium")
    resp = client.put(
        f"/api/account/{account.id}/",
        {"blank": "blank"},
        content_type="application/json",
    )
    assert resp.status_code == 400
