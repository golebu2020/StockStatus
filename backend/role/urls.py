from django.urls import path, include
from .views import CustomUserUpdatePermission
from .views import CustomUserListPermission

# url for updating permissions
urlpatterns = [
    path('<int:pk>/', CustomUserUpdatePermission.as_view(), name="updaet-user-permission" ),
    path('', CustomUserListPermission.as_view(), name="list-user-permission" ),
    
]
