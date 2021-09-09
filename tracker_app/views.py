from rest_framework_simplejwt import authentication
from .models import Tracker
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from .serializers import TrackerSerializer, UserSerializer, GroupSerializer

# Create your views here.
class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]