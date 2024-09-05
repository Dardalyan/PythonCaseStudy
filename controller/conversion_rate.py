from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from serializer.mockupInterviewResult import MockupInterviewResult


class ConversionRate(APIView):

    def get(self,request,**kwargs):
        """
        TASK 2 - Endpoint 1: /api/conversion-rate/: Returns the conversion rate for each customer_id, along with the highest and lowest conversion rates.
        """

        # In response, result data comes from serializer.mockupInterviewResult.MockupInterviewResult() class
        return Response(data={
            'message':'Conversion rate has been calculated for all customers.',
            'result':MockupInterviewResult().conversion_rate_calculation
        },
            status=status.HTTP_200_OK)





