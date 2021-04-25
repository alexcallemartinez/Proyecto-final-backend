from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('categoria', CategoriaController.as_view()),
    path('categoria/<int:id>', CategoriaController.as_view()),
    path('registrocliente', RegistrarUsuarioController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refreshtoken', TokenRefreshView.as_view()),
    path('gasto', RegistrarGastoController.as_view()),
]