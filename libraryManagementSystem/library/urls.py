from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'books/',
        views.books,
        name='books'
    ),

    path(
        'authors/',
        views.authors,
        name='authors'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]