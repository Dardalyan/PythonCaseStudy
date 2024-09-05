from rest_framework.serializers import Serializer
from model.mockupinterview import MockUpInterview


class MockupInterviewResult(Serializer):

    # Conversion Rate Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    conversion_rate_calculation = MockUpInterview.conversionRateWithMinAndMaxRate()

    # Status-based Analysis Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    status_based_analysis = MockUpInterview.revenueAndConversionsPerStatusType()

    # Category And Performance Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    category_and_type_performance = MockUpInterview.categoryAndTypePerformance()

    # Filter and Aggregate Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    filter_and_aggregate = MockUpInterview.filter_and_aggregate()

