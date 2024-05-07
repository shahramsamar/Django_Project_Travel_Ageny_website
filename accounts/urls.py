from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import login_views, logout_views, signup_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = 'accounts'

urlpatterns = [
    # login
    path('login',login_views, name='login'),

    # logout
    path('logout',logout_views, name='logout'),
    
    # registration/sign up
    path('signup',signup_views , name='signup'),
    
    # forgot password
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # template_name='accounts/password_reset.html'
    path('password_reset_confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     # template_name='accounts/password_reset_confirm.html'
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # template_name='accounts/password_reset_complete.html'
     path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'), 
    # template_name='accounts/password_reset_done.html'
]

