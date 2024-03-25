from rest_framework import serializers

from stock.models import Paint



class PaintSerializer(serializers.ModelSerializer):
    """
    Implements the paint serializer for the JSON so that it can be rendered correctly on an interface
    """
    class Meta:
        model = Paint
        fields = ('color', 'availability', 'inventory')

# class CustomUserSerializer(serializers.ModelSerializer):
#     """
#     Implements the CustomUser serializer for the JSON so that it can be rendered correctly on an interface
#     """
#     class Meta:
#         models

