from django.urls import path
from accounts.views import login_views, logout_views, signup_views
# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
    # login
    path('login/',login_views, name='login'),
    # logout
    path('logout/',logout_views, name='logout'),
    # registration/sign up
    path('signup/',signup_views , name='signup'),
    # forgot password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'), 
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
   
]

