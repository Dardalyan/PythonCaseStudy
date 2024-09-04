from django.urls import path
from .conversion_rate import ConversionRate
from .status_based_analysis import StatusBasedAnalysis
from .category_and_type_performance import CategoryAndTypePerformance
from .filtered_aggregation import FilteredAggregation

urlpatterns = [
    path('conversion-rate/', ConversionRate.as_view()),
    path('status-distribution/', StatusBasedAnalysis.as_view()),
    path('category-type-performance/', CategoryAndTypePerformance.as_view()),
    path('filtered-aggregation/', FilteredAggregation.as_view()),
]
