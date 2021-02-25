from django.urls import path
from rest_framework.routers import SimpleRouter

from measurements.views import ProjectViewSet, MeasurementViewSet

router = SimpleRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('measurements', MeasurementViewSet, basename='measurements')

urlpatterns = [] + router.urls
