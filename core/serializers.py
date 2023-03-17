# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import CurrentSpentSummary

# Create a model serializer


class CurrentSpendSummarySerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = CurrentSpentSummary
        fields = ('id', 'cleared_balance', "reward_balance", 'created_at')
