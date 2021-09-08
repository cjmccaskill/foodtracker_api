from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from tracker_app.views import TrackerViewSet

router = routers.DefaultRouter()
router.register(r'tracker', TrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
    
]
