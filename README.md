```
NOTE: In the project files, there are describtions to explain what is happening in those code lines.
```


1) CONVERSION RATE CALCULATION ENDPOINT RESPONSE SCREENSHOT:

   <img width="1505" alt="ConversionRate" src="https://github.com/user-attachments/assets/4d8a7d0b-45f5-41d0-889a-a43071148ac5">

   THE WHOLE CONVERSION RATE CALCULATION ENDPOINT RESPONSE:

 ```
      {
    "message": "Conversion rate has been calculated for all customers.",
    "result": {
        "max_rate": {
            "customer_id": "Customer B",
            "rate": 0.40507348683763306
        },
        "min_rate": {
            "customer_id": "Customer A",
            "rate": 0.3924789161501688
        },
        "all_data": {
            "rates": {
                "Customer A": 0.3924789161501688,
                "Customer B": 0.40507348683763306,
                "Customer C": 0.39358610469787403
            }
        }
    }
}

```


   
2) STATUS-BASED ANALYSIS ENDPOINT RESPONSE SCREENSHOT:

    ```
    NOTE:  "Provides a summary of the distribution of status across different types and categories." As requested here,
            "count" in the JSON response below means how many times these type-category pairs data occur.
    ```
   
   <img width="1505" alt="StatusBased Analysis" src="https://github.com/user-attachments/assets/890f0756-3a2b-4500-a5bc-17c2871542dc">

   <img width="1505" alt="StatusBased Analysis 2" src="https://github.com/user-attachments/assets/0d6394a1-3248-4e63-83e4-50b06a869bad">

    THE WHOLE STATUS-BASED ANALYSIS ENDPOINT RESPONSE:

```
      {
    "message": "Total revenue and total conversions for all status type have been determined.",
    "result": {
        "status": {
            "HIDDEN": {
                "total_revenue": 6558736.779999998,
                "total_conversions": 25916,
                "data": [
                    {
                        "category": "HOME",
                        "type": "ENGAGEMENT",
                        "count": 26
                    },
                    {
                        "category": "HOME",
                        "type": "CONVERSION",
                        "count": 21
                    },
                    {
                        "category": "HOME",
                        "type": "AWARENESS",
                        "count": 16
                    },
                    {
                        "category": "FASHION",
                        "type": "AWARENESS",
                        "count": 32
                    },
                    {
                        "category": "TOYS",
                        "type": "AWARENESS",
                        "count": 26
                    },
                    {
                        "category": "FASHION",
                        "type": "CONVERSION",
                        "count": 26
                    },
                    {
                        "category": "ELECTRONICS",
                        "type": "AWARENESS",
                        "count": 16
                    },
                    {
                        "category": "ELECTRONICS",
                        "type": "ENGAGEMENT",
                        "count": 24
                    },
                    {
                        "category": "TOYS",
                        "type": "ENGAGEMENT",
                        "count": 19
                    },
                    {
                        "category": "ELECTRONICS",
                        "type": "CONVERSION",
                        "count": 15
                    },
                    {
                        "category": "FASHION",
                        "type": "ENGAGEMENT",
                        "count": 20
                    },
                    {
                        "category": "TOYS",
                        "type": "CONVERSION",
                        "count": 15
                    }
                ]
            },
            "ENABLED": {
                "total_revenue": 6121893.329999998,
                "total_conversions": 24439,
                "data": [
                    {
                        "category": "TOYS",
                        "type": "ENGAGEMENT",
                        "count": 24
                    },
                    {
                        "category": "HOME",
                        "type": "ENGAGEMENT",
                        "count": 25
                    },
                    {
                        "category": "TOYS",
                        "type": "AWARENESS",
                        "count": 17
                    },
                    {
                        "category": "ELECTRONICS",
                        "type": "AWARENESS",
                        "count": 26
                    },
                    {
                        "category": "TOYS",
                        "type": "CONVERSION",
                        "count": 17
                    },
                    {
                        "category": "FASHION",
                        "type": "AWARENESS",
                        "count": 24
                    },
                    {
                        "category": "FASHION",
                        "type": "CONVERSION",
                        "count": 26
                    },
                    {
                        "category": "FASHION",
                        "type": "ENGAGEMENT",
                        "count": 18
                    },
                    {
                        "category": "ELECTRONICS",
                        "type": "CONVERSION",
                        "count": 19
                    },
                    {
                        "category": "ELECTRONICS",
                        "type": "ENGAGEMENT",
                        "count": 20
                    },
                    {
                        "category": "HOME",
                        "type": "AWARENESS",
                        "count": 15
                    },
                    {
                        "category": "HOME",
                        "type": "CONVERSION",
                        "count": 13
                    }
                ]
            }
        }
    }
}
 ```

   
3) CATEGORY AND TYPE PERFORMANCE ENDPOINT RESPONSE SCREENSHOT:

   ![CategoryAndType Performance.png](..%2F..%2FCategoryAndType%20Performance.png)

    THE WHOLE CATEGORY AND TYPE PERFORMANCE ENDPOINT RESPONSE:

```
      {
    "message": "Total revenue and total conversions have been calculated for all combinations and (category-type) combination that generates the most conversions has been identified.",
    "result": {
        "top_performed_conversion": {
            "('FASHION', 'CONVERSION')": {
                "total_conversion": 5271,
                "total_revenue": 1415989.9500000002
            }
        },
        "all_combined_data": {
            "('FASHION', 'ENGAGEMENT')": {
                "total_conversion": 3625,
                "total_revenue": 1222168.42
            },
            "('FASHION', 'AWARENESS')": {
                "total_conversion": 5119,
                "total_revenue": 1301353.4100000001
            },
            "('ELECTRONICS', 'AWARENESS')": {
                "total_conversion": 3782,
                "total_revenue": 1145380.7700000003
            },
            "('ELECTRONICS', 'CONVERSION')": {
                "total_conversion": 3448,
                "total_revenue": 720999.9100000001
            },
            "('HOME', 'CONVERSION')": {
                "total_conversion": 3829,
                "total_revenue": 865975.6399999998
            },
            "('TOYS', 'ENGAGEMENT')": {
                "total_conversion": 4199,
                "total_revenue": 985486.8200000001
            },
            "('FASHION', 'CONVERSION')": {
                "total_conversion": 5271,
                "total_revenue": 1415989.9500000002
            },
            "('TOYS', 'CONVERSION')": {
                "total_conversion": 3323,
                "total_revenue": 809981.13
            },
            "('HOME', 'ENGAGEMENT')": {
                "total_conversion": 5036,
                "total_revenue": 1223794.8299999998
            },
            "('ELECTRONICS', 'ENGAGEMENT')": {
                "total_conversion": 4952,
                "total_revenue": 1168029.5000000002
            },
            "('TOYS', 'AWARENESS')": {
                "total_conversion": 4025,
                "total_revenue": 1049368.3799999997
            },
            "('HOME', 'AWARENESS')": {
                "total_conversion": 3746,
                "total_revenue": 772101.35
            }
        }
    }
}

```

   
4) FILTER AND AGGREGATE ENDPOINT RESPONSE SCREENSHOT:
   
    ![FilterAndAggregate.png](..%2F..%2FFilterAndAggregate.png)

   THE WHOLE FILTER AND AGGREGATE ENDPOINT RESPONSE:

```
      {
    "message": "Dataset filtering by the type which is CONVERSION, filtered dataset aggregation, average revenue and average conversions per customer_id have been provided. ",
    "result": {
        "average": {
            "Customer A": {
                "average_revenue": 26084.47520833333,
                "average_conversions": 105.14583333333333
            },
            "Customer B": {
                "average_revenue": 24771.766250000008,
                "average_conversions": 112.19642857142857
            },
            "Customer C": {
                "average_revenue": 24451.518958333338,
                "average_conversions": 94.60416666666667
            }
        },
        "all_aggregated_data": [
            {
                "customer_id": "Customer C",
                "revenue": 4684.36,
                "conversions": 82,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 39288.05,
                "conversions": 37,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 25246.31,
                "conversions": 158,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 13268.92,
                "conversions": 21,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 15933.77,
                "conversions": 28,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 12145.01,
                "conversions": 103,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 16737.09,
                "conversions": 171,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 24160.55,
                "conversions": 101,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 29876.97,
                "conversions": 44,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 41916.26,
                "conversions": 43,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 17686.53,
                "conversions": 123,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 38358.59,
                "conversions": 189,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 22488.41,
                "conversions": 24,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 22955.99,
                "conversions": 29,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 32169.12,
                "conversions": 41,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 47603.8,
                "conversions": 15,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 47756.13,
                "conversions": 40,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 6759.47,
                "conversions": 7,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 42721.11,
                "conversions": 95,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 4877.59,
                "conversions": 40,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 19955.5,
                "conversions": 131,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 5034.87,
                "conversions": 196,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 27897.78,
                "conversions": 36,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 35648.06,
                "conversions": 111,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 43389.79,
                "conversions": 183,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 5930.02,
                "conversions": 168,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 6108.08,
                "conversions": 103,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 43593.84,
                "conversions": 29,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 14050.06,
                "conversions": 10,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 10281.02,
                "conversions": 112,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 22473.44,
                "conversions": 58,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 10769.91,
                "conversions": 55,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 30384.05,
                "conversions": 114,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 48479.08,
                "conversions": 81,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 15589.86,
                "conversions": 162,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 1989.8,
                "conversions": 130,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 42150.85,
                "conversions": 163,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 34475.41,
                "conversions": 182,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 13035.44,
                "conversions": 41,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 42515.3,
                "conversions": 48,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 8413.51,
                "conversions": 189,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 15004.5,
                "conversions": 45,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 29223.86,
                "conversions": 37,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 1415.01,
                "conversions": 15,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 27888.29,
                "conversions": 197,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 15912.5,
                "conversions": 84,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 33298.05,
                "conversions": 172,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 22821.44,
                "conversions": 109,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 18974.28,
                "conversions": 127,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 24505.64,
                "conversions": 97,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 1106.53,
                "conversions": 78,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 32156.67,
                "conversions": 182,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 16894.45,
                "conversions": 185,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 8068.93,
                "conversions": 19,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 21064.76,
                "conversions": 122,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 32392.79,
                "conversions": 29,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 13745.93,
                "conversions": 179,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 18954.81,
                "conversions": 169,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 9898.51,
                "conversions": 53,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 27619.22,
                "conversions": 60,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 49063.47,
                "conversions": 185,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 42289.05,
                "conversions": 145,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 8249.48,
                "conversions": 103,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 48422.54,
                "conversions": 188,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 5511.87,
                "conversions": 191,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 23591.45,
                "conversions": 154,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 37754.37,
                "conversions": 68,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 43692.66,
                "conversions": 73,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 42853.52,
                "conversions": 98,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 49838.0,
                "conversions": 71,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 21519.91,
                "conversions": 154,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 30638.01,
                "conversions": 68,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 17095.36,
                "conversions": 192,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 43378.85,
                "conversions": 156,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 39970.62,
                "conversions": 70,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 19435.09,
                "conversions": 158,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 27180.03,
                "conversions": 60,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 17726.62,
                "conversions": 177,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 20507.63,
                "conversions": 46,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 17718.89,
                "conversions": 88,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 33112.35,
                "conversions": 67,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 6928.05,
                "conversions": 82,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 28299.61,
                "conversions": 9,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 19481.82,
                "conversions": 70,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 46255.9,
                "conversions": 192,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 16060.47,
                "conversions": 199,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 39741.75,
                "conversions": 35,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 29194.35,
                "conversions": 67,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 47642.93,
                "conversions": 48,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 47393.58,
                "conversions": 74,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 35589.75,
                "conversions": 107,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 38126.34,
                "conversions": 126,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 26455.54,
                "conversions": 159,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 1708.3,
                "conversions": 189,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 14226.32,
                "conversions": 190,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 25771.84,
                "conversions": 61,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 11247.9,
                "conversions": 30,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 22196.11,
                "conversions": 165,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 16822.17,
                "conversions": 95,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 3176.98,
                "conversions": 67,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 31765.79,
                "conversions": 144,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 49853.01,
                "conversions": 122,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 30035.77,
                "conversions": 1,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 6655.02,
                "conversions": 100,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 29814.03,
                "conversions": 87,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 31946.37,
                "conversions": 185,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 3690.2,
                "conversions": 164,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 39185.49,
                "conversions": 10,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 48435.95,
                "conversions": 55,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 32129.34,
                "conversions": 153,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 34985.43,
                "conversions": 110,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 31696.97,
                "conversions": 169,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 42258.9,
                "conversions": 127,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 37509.33,
                "conversions": 74,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 18322.17,
                "conversions": 174,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 23331.6,
                "conversions": 150,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 15231.72,
                "conversions": 188,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 13607.84,
                "conversions": 57,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 4256.41,
                "conversions": 189,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 47125.28,
                "conversions": 158,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 18752.87,
                "conversions": 16,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 19101.27,
                "conversions": 196,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 35505.65,
                "conversions": 198,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 42009.3,
                "conversions": 183,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 45068.84,
                "conversions": 64,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 33398.69,
                "conversions": 187,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 2941.33,
                "conversions": 144,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 38351.15,
                "conversions": 69,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 22358.22,
                "conversions": 110,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 16385.21,
                "conversions": 72,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 47874.13,
                "conversions": 151,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 12003.63,
                "conversions": 67,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 2791.31,
                "conversions": 105,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 42108.98,
                "conversions": 37,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 1193.57,
                "conversions": 179,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 17051.12,
                "conversions": 153,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 18894.53,
                "conversions": 70,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 38519.98,
                "conversions": 121,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 18821.32,
                "conversions": 115,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 24706.98,
                "conversions": 100,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 17700.04,
                "conversions": 38,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 30732.25,
                "conversions": 164,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 27912.04,
                "conversions": 71,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 12306.75,
                "conversions": 42,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 24631.51,
                "conversions": 8,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 21565.17,
                "conversions": 31,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 45571.01,
                "conversions": 121,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 11084.23,
                "conversions": 31,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer A",
                "revenue": 8566.86,
                "conversions": 196,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 2875.57,
                "conversions": 93,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer C",
                "revenue": 27779.03,
                "conversions": 172,
                "type": "CONVERSION"
            },
            {
                "customer_id": "Customer B",
                "revenue": 36932.12,
                "conversions": 21,
                "type": "CONVERSION"
            }
        ]
    }
}

   ```
