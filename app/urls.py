from django.urls import path
from .views import get_users_by_category, get_users_all

urlpatterns = [
    # Other paths...
    path('get_users_by_category/', get_users_by_category, name='get_users_by_category'),
    path('get_users_all/', get_users_all, name='get_users_all'),
]
