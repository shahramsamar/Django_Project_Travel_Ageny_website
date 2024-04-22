from django.urls import path
from accounts.views import login_views, logout_views, signup_views


app_name = 'accounts'

urlpatterns = [
    # login
    path('login',login_views, name='login'),

    # logout
    path('logout',logout_views, name='logout'),
    
    # register/sign up
    path('signup',signup_views , name='signup'),

    # forgot password
    # path('forgot_password',forgot_password_views , name='forgot_password'),


]