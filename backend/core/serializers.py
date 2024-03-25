from rest_framework import serializers

from stock.models import Paint


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = ('color', 'availability', 'inventory')
