from rest_framework import viewsets, generics
from . import serializers
from . import models


# class ProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint for projects
#     """
#     queryset = models.Project.objects.all().order_by('-id')
#     serializer_class = serializers.ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer