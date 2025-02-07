from django.urls import path
from . import views

urlpatterns = [
    #URL del index
    path('user/', views.list_users),
    path('user/<str:username>/', views.mod_users),
    #path('register/', views.register),
    path('login/', views.loginvw, name='login'),
    path('user/<str:username>/subdelegacion', views.subdelega_edit),
]
