from django.urls import path
from . import views

urlpatterns = [
    path('api/games/', views.GameCreate.as_view() ),
    path('api/players/', views.PlayerCreate.as_view() ),
]