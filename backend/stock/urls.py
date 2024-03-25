from django.urls import path, include
from .views import PaintList, PaintModify


urlpatterns = [
    path('', PaintList.as_view(), name='paint-list-create'),
    path('<int:pk>/', PaintModify.as_view(), name = 'paint-patch')
]
