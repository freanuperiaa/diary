
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('apps.diary.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
