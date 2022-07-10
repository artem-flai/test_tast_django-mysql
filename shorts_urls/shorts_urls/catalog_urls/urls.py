from django.urls import path
from .views import *

urlpatterns = [
    path('', Reg.as_view(), name='reg'),
    path('log_in/', LogIn.as_view(), name='log_in'),
    path('logout/', logout_user, name='logout'),
    path('create_shorts_url/', create_shorts_url, name='create_shorts_url'),
    path('catalog_urls/', catalog_urls, name='catalog_urls'),
    path('short_u/<slug:url_s>/', short_u, name='short_u'),
]