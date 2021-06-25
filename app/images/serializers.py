from rest_framework import serializers
from .models import Account, User, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    account_type = AccountSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'account_type']
        read_only_fields = ('id',)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'image',
            'user_id',
        )
