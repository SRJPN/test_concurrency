from django.shortcuts import render
from rest_framework import viewsets

from core.models import CurrentSpentSummary
from core.serializers import CurrentSpendSummarySerializer

# Create your views here.

class CurrentSpendSummaryViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = CurrentSpentSummary.objects.all()
     
    # specify serializer to be used
    serializer_class = CurrentSpendSummarySerializer