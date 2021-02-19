from rest_framework import serializers
from .models import *


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
