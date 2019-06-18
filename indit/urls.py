
from django.contrib import admin
from django.urls import path,include
from home import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('employees/', include('employees.urls')),
]
