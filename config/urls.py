from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('helper/', include('app.urls')),
    path('', admin.site.urls),
]
