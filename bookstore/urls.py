from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.viewsets import BookViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
