from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Book, Author


def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(
                request,
                'register.html',
                {'error': 'Passwords do not match'}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'register.html',
                {'error': 'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def books(request):

    search = request.GET.get('search')

    if search:
        books = Book.objects.filter(
            title__icontains=search
        )
    else:
        books = Book.objects.all()

    return render(
        request,
        'books.html',
        {'books': books}
    )


def authors(request):

    authors = Author.objects.all()

    return render(
        request,
        'authors.html',
        {'authors': authors}
    )


def logout_view(request):

    logout(request)

    return redirect('login')