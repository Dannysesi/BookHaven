from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    # path('book/<int:pk>/', BookDetailView.as_view(), name='post-detail')
]