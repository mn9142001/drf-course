from django.urls import path
from .views import posts_list

urlpatterns = [
    path('list', posts_list)
]
