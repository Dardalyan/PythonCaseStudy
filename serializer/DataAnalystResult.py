from rest_framework.serializers import Serializer
from model.DataAnalyst import DataAnalyst


class DataAnalystResult(Serializer):

    # Conversion Rate Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    conversion_rate_calculation = DataAnalyst.conversionRateWithMinAndMaxRate()

    # Status-based Analysis Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    status_based_analysis = DataAnalyst.revenueAndConversionsPerStatusType()

    # Category And Performance Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    category_and_type_performance = DataAnalyst.categoryAndTypePerformance()

    # Filter and Aggregate Result as dictionary to be able to be convertable to JSON, which is taken from MockUpInterview class
    filter_and_aggregate = DataAnalyst.filter_and_aggregate()

