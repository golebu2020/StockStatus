
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('manager/', admin.site.urls),
    path('api/', include('stock.urls'), name='stock-api'),
]
