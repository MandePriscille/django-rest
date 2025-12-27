from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewset

router = DefaultRouter()
router.register(' ', ProductViewset, basename='product-a')

print(router.urls)
urlpatterns = router.urls

