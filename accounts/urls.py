from django.urls import path
from accounts.views import login_view



app_name = 'accounts'

urlpatterns = [
    # login
    path('login',login_view , name='login'),

    # logout
    # path('logout',logout_view , name='login'),
    
    # register/sign up
    # path('signup',signup_view , name='login'),

    # forgot password
    # path('forgot_password',forgot_password_view , name='forgot_password'),


]