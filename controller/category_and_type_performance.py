from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from serializer.mockupInterviewResult import MockupInterviewResult


class CategoryAndTypePerformance(APIView):

    def get(self,request,**kwargs):
        """
        TASK 2 - Endpoint 3: /api/conversion-rate/: Returns the total revenue and conversions grouped by category and type. And also returns the top-performing category and type combination.
        """

        return Response(data={
            'message':'Total revenue and conversions has been calculated AND (category-type) combination that generates the most conversions has been identified.',
            'result':MockupInterviewResult().category_and_type_performance
        },
            status=status.HTTP_200_OK)








