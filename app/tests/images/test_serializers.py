from images.serializers import AccountSerializer, UserSerializer, ImageSerializer
from images.models import Account, Image, User
import pytest

def test_valid_account_serializer():
    valid_serializer_data = {
        "name": "Basic"
    }
    serializer = AccountSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_account_serializer():
    invalid_serializer_data = {

    }
    serializer = AccountSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}


def test_valid_user_serializer():
    valid_serializer_data = {
        "username": "XYZ",
    }
    serializer = UserSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_user_serializer():

    invalid_serializer_data = {

    }
    serializer = UserSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == invalid_serializer_data
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"username": ['This field is required.']}


@pytest.mark.django_db
def test_valid_image_serializer():
    account = Account(name="Basic")
    account.save()
    user = User(username="XYZ", account_type=account)

    user.save()
    image = Image.objects.create(
        image='images/image.jpg',
        user_id=user
    )
    image.save()
    serialized_data = ImageSerializer(image)
    assert serialized_data['user_id']
    assert serialized_data['image']
