from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.PostListView.as_view(), name=None),
    path('create/', views.PostCreateView.as_view(), name=None),
    path('<int:pk>/', views.PostDetailView.as_view(), name=None)
]