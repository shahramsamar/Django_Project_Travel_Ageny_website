from django.urls import path
from website.views import index_view, about_view, contact_view, newsletter_view, test_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name="about"),
    path('contact', contact_view, name='contact'),
    path('newsletter', newsletter_view, name='newsletter'),
    path('test', test_view, name='test'),


]
