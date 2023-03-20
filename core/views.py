from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import CurrentSpentSummary, CurrentSpentSummaryRegister
from core.serializers import CurrentSpendSummarySerializer

# Create your views here.


class CurrentSpendSummaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the current spend summary items.
        '''
        list = CurrentSpentSummary.objects.all()
        serializer = CurrentSpendSummarySerializer(list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the current spend summary
        '''

        created = CurrentSpentSummary.objects.create(
            cleared_balance=request.data.get('cleared_balance'),
            reward_balance=request.data.get('reward_balance')
        )
        CurrentSpentSummaryRegister.objects.create(
            current_spent_summary_id=created.id,
            reward_balance=request.data.get('reward_balance'),
            cleared_balance=request.data.get('cleared_balance'),
        )
        return Response(CurrentSpendSummarySerializer(created).data, status=status.HTTP_201_CREATED)


class CurrentSpendSummaryDetailAPIView(APIView):
    def put(self, request, id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        current_spend_summary = CurrentSpentSummary.objects.get(pk=id)
        if not current_spend_summary:
            return Response(
                {"res": f"CurrentSpentSummary with {id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        CurrentSpentSummaryRegister.objects.create(
            current_spent_summary_id=id,
            reward_balance=request.data.get('reward_balance'),
            cleared_balance=request.data.get('cleared_balance'),
        )
        updated = CurrentSpentSummary.objects.update_current_spent_summary(id,
                                                                           request.data.get(
                                                                               'reward_balance'),
                                                                           request.data.get('cleared_balance'))
        return Response(CurrentSpendSummarySerializer(updated).data, status=status.HTTP_201_CREATED)
