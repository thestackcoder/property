from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter()
# router.register(r'projects', views.ProjectViewSet, basename='projects')

urlpatterns = [
    # path('', include(router.urls)),
    path('projects/', views.ProjectList.as_view(), name='project-list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)