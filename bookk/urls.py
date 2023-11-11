"""
URL configuration for bookk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_view
from books import views as book_view
from django.conf import settings
from django.conf.urls.static import static
from books.views import BookCreateView, BookUpdateView, BookDeleteView
from books.admin import admin_site
from users.views import BookListView

urlpatterns = [
    # Users app
    path('admin/', admin_site.urls, name='admin'),
    path('register/', user_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', user_view.base, name='home-page'),
    path('profile/', user_view.profile, name="profile"),

    # Books app
    path('', include('books.urls')),
    path('book_list/', book_view.book_list, name='book_list'),
    path('books/genre/<str:genre_type>', book_view.books_by_genre, name='books_by_genre'),
    path('books/<int:id>/submit_review/', book_view.submit_review, name='submit_review'),
    path('search/', book_view.book_search, name='search'),


    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    #password reset
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-comfirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)