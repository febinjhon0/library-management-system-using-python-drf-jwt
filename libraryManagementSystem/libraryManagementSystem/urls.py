from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from library.api_views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()

router.register(
    'authors',
    AuthorViewSet
)

router.register(
    'books',
    BookViewSet
)

router.register(
    'borrow',
    BorrowViewSet
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('library.urls')),

    path(
        'api/',
        include(router.urls)
    ),

    path(
        'api/token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view()
    ),
]