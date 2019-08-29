from rest_framework import serializers
from .models import Poets


class poetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poets
        fields = '__all__'
