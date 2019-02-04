from django.contrib import admin
from django.urls import path, re_path, include
#from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include('data.urls')),
]
