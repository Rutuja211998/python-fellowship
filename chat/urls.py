from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('activate/<str:token>', views.activate, name="activate"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', views.LoginView.as_view(), name="signup"),
    path('reset/<str:token>', views.ResetPassword, name="reset"),
    ]

