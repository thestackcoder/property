from rest_framework import serializers
from . import models

class LongTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LargeText
        fields = ['id', 'title', 'image', 'text']

class ProjectSerializer(serializers.ModelSerializer):
    largetext = LongTextSerializer(many=True, read_only=True)
    class Meta:
        model = models.Project
        fields = ['id', 'title', 'cover', 'description', 'brochure', 'created_on', 'largetext']
