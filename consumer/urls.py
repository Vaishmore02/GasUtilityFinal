# urls.py
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home_view, name='home'),
    # path('login/', login_view, name='login'),
    # path('register/', register_view, name='register'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),
    
    # Add other URLs as needed
]
