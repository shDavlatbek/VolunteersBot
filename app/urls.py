from django.urls import path
from .views import get_users_by_category

urlpatterns = [
    # Other paths...
    path('get_users_by_category/', get_users_by_category, name='get_users_by_category'),
]
