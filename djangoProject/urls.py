from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('risks/', include('risks.urls')),
    path('notifications/', include('notifications.urls')),
]