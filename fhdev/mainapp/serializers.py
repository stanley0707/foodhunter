from rest_framework import serializers
from .models import (
    ChatRoom,
    Chat,)
from accounts.models import User, EmailActivation


class UserSerializers(serializers.ModelSerializer):
    """ User  serializers.ModelSerializer """

    class Meta:
        model = User
        depth = 10
        fields = ('id', 'email', 'first_name', 'last_name')

class ChatRoomSerializers(serializers.ModelSerializer):
    """ Serialize a chatroom model"""
    
    creator = UserSerializers()
    invited = UserSerializers(many=True)
    
    class Meta:
        model =  ChatRoom
        depth = 5
        fields = ('id', 'creator', 'invited', 'date')

class ChatSerializers(serializers.ModelSerializer):
    """ Chat serialize GET  """
    
    user = UserSerializers()
    
    class Meta:
        model = Chat
        depth = 5
        fields = ('user', 'text', 'date',)

class ChatPostSerializers(serializers.ModelSerializer):
    """ Chat serialize POST 
        get room ( messege id ) and self text
    """
    class Meta:
        model = Chat
        depth = 5
        fields = ('room', 'text')

class EmailActivateSerializers(serializers.ModelSerializer):
    """ Serialize email Key Activation """

    class Meta:
        model = EmailActivation
        fields = ('user', 'email', 'key')


class UserRegistrSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'ckook', 'password')

    def create(self, validated_data):
        user = super(UserRegistrSerializers, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 5
        fields = ('account',)
