from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from serializer.mockupInterviewResult import MockupInterviewResult


class FilteredAggregation(APIView):

    def get(self,request,**kwargs):
        """
        TASK 2 - Endpoint 4: /api/filtered-aggregation/: Returns all aggregated data where type is CONVERSION and returns the average revenue and conversions per customer_id.
        """

        return Response(data={
            'message':'Dataset filtering by the type is CONVERSION, filtered set aggregation and avg. revenue and conversions per customer_id has been provided. ',
            'result':MockupInterviewResult().filter_and_aggregate
        },
            status=status.HTTP_200_OK)







