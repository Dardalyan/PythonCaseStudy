from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from serializer.DataAnalystResult import DataAnalystResult


class StatusBasedAnalysis(APIView):


    def get(self,request,**kwargs):
        """
        TASK 2 - Endpoint 2: /api/status-distribution/: Provides a summary of the distribution of status across different types and categories. And also includes total revenue and conversions for each status.
        """

        # In response, result data comes from serializer.mockupInterviewResult.MockupInterviewResult() class
        return Response(data={
            'message':'Total revenue and total conversions for all status type have been determined.',
            'result':DataAnalystResult().status_based_analysis
        },
            status=status.HTTP_200_OK)








