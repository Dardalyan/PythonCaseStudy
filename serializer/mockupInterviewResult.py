from rest_framework.serializers import Serializer
from model.mockupinterview import MockUpInterview


class MockupInterviewResult(Serializer):

    conversion_rate_calculation = MockUpInterview.conversionRateWithMinAndMaxRate()
    status_based_analysis = MockUpInterview.revenueAndConversionsPerStatusType()
    category_and_type_performance = MockUpInterview.categoryAndTypePerformance()
    filter_and_aggregate = MockUpInterview.filter_and_aggregate()

