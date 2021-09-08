from .models import Tracker
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class TrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tracker
        fields = ['id', 'title', 'image', 'servings', 'calories']