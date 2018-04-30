from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('manga.urls')),
    path('api/', include('rest_auth.urls')),
    path('api/registration/', include('rest_auth.registration.urls'))
]
