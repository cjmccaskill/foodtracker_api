from django.db.models import fields
from .models import Tracker
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class TrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tracker
        fields = ['id', 'title', 'image', 'servings', 'calories']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']