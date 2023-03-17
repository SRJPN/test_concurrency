
# basic URL Configurations
from django.urls import path
 
# import everything from views
from .views import *
 
# specify URL Path for rest_framework
urlpatterns = [
    path('current-spend-summary', CurrentSpendSummaryAPIView.as_view()),
    path('current-spend-summary/<str:id>', CurrentSpendSummaryDetailAPIView.as_view()),
]