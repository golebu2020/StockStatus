from django.urls import path, include
from .views import PaintList


urlpatterns = [
    path('', PaintList.as_view(), name='list-create'),
]
