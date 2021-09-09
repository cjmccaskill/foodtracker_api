from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers, views
from tracker_app.views import TrackerViewSet, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'tracker', TrackerViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
    
]
