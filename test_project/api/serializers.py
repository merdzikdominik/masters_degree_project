from rest_framework import serializers
from .models import Annual

class AnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annual

        fields = ('__all__')

