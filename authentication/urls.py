from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', views.signupView, name="signup"),
    path('logout', views.logoutView, name="logout"),
]
