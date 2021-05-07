from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from carts.views import CartItemViewSet
from foodshop.utils import schema_view
from items.views import ItemViewSet


router = DefaultRouter()
router.register('items', ItemViewSet, basename='items')
router.register('carts/items', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('carts.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/users/', include('users.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
