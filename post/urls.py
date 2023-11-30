from django.urls import path
from .views import PostReadViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', PostReadViewSet)

urlpatterns = [

] + router.urls
