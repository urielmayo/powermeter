from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'electricmeters', views.ElectricMeterViewSet, basename='electricmeters')
router.register(r'electricmeasures', views.ElectricMeasureViewSet, basename='electricmeasures')
urlpatterns = router.urls