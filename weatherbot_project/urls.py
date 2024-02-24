from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherbot/', include('weatherbot.urls')),  # Include weatherbot app URLs
]

