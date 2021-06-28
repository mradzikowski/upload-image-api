import pytest

from images.models import Account, Image, User


@pytest.mark.django_db
def test_account_model():
    account = Account(name="Basic")
    account.save()
    assert account.name == "Basic"
    assert str(account) == "Basic"


@pytest.mark.django_db
def test_user_model():
    account = Account(name="Basic")
    user = User(username="XYZ", account_type=account)
    account.save()
    user.save()
    assert user.username == "XYZ"
    assert str(user) == "XYZ"
    assert user.account_type


@pytest.mark.django_db
def test_image_model():
    account = Account(name="Basic")
    account.save()
    user = User(username="XYZ", account_type=account)
    user.save()
    image = Image(user_id=user)
    image.save()

    assert image.user_id == user
    assert str(image) == str(user)
