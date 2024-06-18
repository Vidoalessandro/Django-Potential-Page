from django.urls import path
from .views import HomeView, LogoutView, SigninView, CustomLoginView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
