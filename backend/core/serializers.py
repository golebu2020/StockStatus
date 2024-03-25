from rest_framework import serializers

from stock.models import Paint
from role.models import CustomUser



class PaintSerializer(serializers.ModelSerializer):
    """
    Implements the paint serializer for the JSON so that it can be rendered correctly on an interface
    """
    class Meta:
        model = Paint
        fields = ('color', 'availability', 'inventory')

class CustomUserPermissionSerializer(serializers.ModelSerializer):
    """
    Implements the CustomUser serializer for the JSON so that it can be rendered correctly on an interface
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'can_view_paint', 'can_edit_paint', 'can_access')