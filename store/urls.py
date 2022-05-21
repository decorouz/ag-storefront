from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)


urlpatterns = router.urls
