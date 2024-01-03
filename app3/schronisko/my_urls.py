from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'animals', views.AnimalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
