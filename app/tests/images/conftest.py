import pytest

from images.models import Account


@pytest.fixture(scope='function')
def add_account():
    def _add_account(name):
        account = Account.objects.create(name=name)
        return account
    return _add_account
