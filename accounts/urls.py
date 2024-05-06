from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import ResetPasswordView, login_views, logout_views, signup_views
# from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


app_name = 'accounts'

urlpatterns = [
    # login
    path('login',login_views, name='login'),

    # logout
    path('logout',logout_views, name='logout'),
    
    # registration/sign up
    path('signup',signup_views , name='signup'),
    
    # forgot password
    path('password-reset/', ResetPasswordView.as_view(), name='password-reset'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),

     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

