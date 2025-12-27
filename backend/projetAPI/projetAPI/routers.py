from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewset, ProductListRetrive

router = DefaultRouter()
router.register('', ProductViewset, basename='product-a')
router.register('list/retrieve', ProductListRetrive, basename='product-list-retrieve')

urlpatterns = router.urls

