from rest_framework import serializers 

from .models import TestModel


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "body"
        )
        model = TestModel
