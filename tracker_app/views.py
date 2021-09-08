from .models import Tracker
from rest_framework import viewsets, permissions
from .serializers import TrackerSerializer

# Create your views here.
class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = [permissions.AllowAny]