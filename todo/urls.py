from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('todos', ToDoListView)

urlpatterns = [
    path('', include(router.urls)),
]
