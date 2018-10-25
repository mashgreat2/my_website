from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet

router = DefaultRouter()
router.register('', CompanyViewSet, basename='companies')
urlpatterns = router.urls