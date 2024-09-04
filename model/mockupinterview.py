import pandas as pd


# TASK 1 : For the "TASK 1" , I've created a class with name 'MockUpInterview' AND
#          I handled all the subtasks such as 'Conversion Rate Calculation' : in some spesific purposed classmethods


class MockUpInterview:

    __dataSet = pd.read_csv('mockupinterviewdata.csv') #Keys->['customer_id', 'revenue', 'conversions', 'status', 'type', 'category','date', 'impressions', 'clicks']

    __customer_id_list = sorted(list(set(__dataSet['customer_id']))) # [Customer A, Customer B, Customer C]

    __statusTypes = sorted(list(set(__dataSet['status']))) # [ENABLED, HIDDEN]

    __categories = sorted(list(set(__dataSet['category']))) # ['ELECTRONICS', 'FASHION', 'HOME', 'TOYS']

    __types = sorted(list(set(__dataSet['type']))) # ['AWARENESS', 'CONVERSION', 'ENGAGEMENT']

    @classmethod
    def __get_dataset__(cls):
        """
        :return: All the data_set as type of pd.DataFrame
        """
        return cls.__dataSet



    @classmethod
    def __numOfConversions(cls,customer_id:str):
        """
            TASK 1 - 1) Conversion Rate Calculation: Calculates the number of conversions for the given customer_id and returns the total number of conversions.
        """

        total = 0
        for id, conversion in zip(cls.__dataSet['customer_id'], cls.__dataSet['conversions']):
            if id == customer_id:
                total += conversion

        #print(f"{customer_id} 's Total Conversion calculated as {total} !") #->  A: 17129, B: 17424, C:15802
        return total

    @classmethod
    def __numOfRevenue(cls,customer_id:str):
        """
            TASK 1 - 1) Conversion Rate Calculation: Calculates the number of revenue for the given customer_id and returns the total number of revenues.
        """

        total = 0
        for id, revenue in zip(cls.__dataSet['customer_id'], cls.__dataSet['revenue']):
            if id == customer_id:
                total += revenue
        #print(f"{customer_id} 's Total Revenue calculated as {total} !") #->  A: 4364310.87 , B: 4301441.729999999, C:4014877.5100000007

        return total

    @classmethod
    def __conversion_rate_cal(cls):
        """
          TASK 1 - 1) Conversion Rate Calculation: Calculates the ratio of conversions to revenue.
        """
        totals = {
            'Customer A':None,
            'Customer B':None,
            'Customer C':None
        }

        for i in totals.keys():
            totals[i] = (cls.__numOfConversions(i) / cls.__numOfRevenue(i))*100

        #print(f"-> The ratio per customer {totals}") #-> The ratio per customer {'Customer A': 0.3924789161501688, 'Customer B': 0.40507348683763306, 'Customer C': 0.39358610469787403}


        return totals

    @classmethod
    def conversionRateWithMinAndMaxRate(cls):
        """
        TASK 1 - Conversion Rate Calculation:
        Identifies the customer who has the maximum and the minimum ratio AND returns also the all ratio data.
        """
        rates = cls.__conversion_rate_cal()

        maxRate = max(rates.values())
        minRate = min(rates.values())


        find_id = lambda x: cls.__customer_id_list[0] if x == rates[cls.__customer_id_list[0]] else cls.__customer_id_list[1]\
            if x == rates[cls.__customer_id_list[1]] else cls.__customer_id_list[2]\
            if x == rates[cls.__customer_id_list[2]] else None


        customer_id_with_max = find_id(maxRate)
        customer_id_with_min = find_id(minRate)

        result = {
            'max_rate':{
                'customer_id':customer_id_with_max,
                'rate':maxRate
            },
            'min_rate':{
                'customer_id': customer_id_with_min,
                'rate': minRate
            },
            'all_data':{
                'rates':rates
            }
        }

        return result

    @classmethod
    def revenueAndConversionsPerStatusType(cls):
        """
        TASK 1 - 2) Status-Based Analysis: Determines the total revenue and conversions per status.
        """
        hidden = {'total_revenue': 0, 'total_conversions': 0, 'data': set()}
        enabled = {'total_revenue': 0, 'total_conversions': 0, 'data': set()}

        temp_enabled = []
        temp_hidden = []

        for status, revenue, conversion, category, typ in zip(cls.__dataSet['status'], cls.__dataSet['revenue'],
                                                              cls.__dataSet['conversions'], cls.__dataSet['category'],
                                                              cls.__dataSet['type']):
            if status == cls.__statusTypes[1]:
                hidden['total_revenue'] += revenue
                hidden['total_conversions'] += conversion
                temp_hidden.append((category, typ))
            if status == cls.__statusTypes[0]:
                enabled['total_revenue'] += revenue
                enabled['total_conversions'] += conversion
                temp_enabled.append((category, typ))

        for i in temp_hidden:
            hidden['data'].add((i[0], i[1], temp_hidden.count(i)))

        for i in temp_enabled:
            enabled['data'].add((i[0], i[1], temp_enabled.count(i)))

        hidden['data'] = list(hidden['data'])
        enabled['data'] = list(enabled['data'])

        # Converting tuples into dictionary and adding them in to the list
        hidden['data'] = [{'category': i[0], 'type': i[1], 'count': i[2]} for i in hidden['data']]
        enabled['data'] = [{'category': i[0], 'type': i[1], 'count': i[2]} for i in enabled['data']]

        #print(f"->The total revenue and conversions with status = {cls.__statusTypes[0]} : {enabled['total_revenue']}  and {enabled['total_conversions']} \n ->The all data with Status = {cls.__statusTypes[0]}  : {enabled['data']} ")
        #print(f"->The total revenue and conversions with status = {cls.__statusTypes[1]} : {hidden['total_revenue']}  and {hidden['total_conversions']} \n ->The all data with Status = {cls.__statusTypes[1]}  : {hidden['data']} ")


        return {
            'status': {
                'HIDDEN': hidden,
                'ENABLED': enabled
            }
        }

    @classmethod
    def categoryAndTypePerformance(cls):
        """
        TASK 1 - 3) Category and Type Performance: Calculates the total revenue and total conversions grouped by category and type.
                    AND Identifies the category and type combination that generates the most conversions.
        """

        total_revenue = {'total_revenue_per_category':{},'total_revenue_per_type':{}}
        total_conversion = {'total_conversion_per_category': {},'total_conversion_per_type': {}}

        combinationOfTheMostConvs = {}

        for cat_name in cls.__categories:
            total_revenue['total_revenue_per_category'][cat_name] = 0
            total_conversion['total_conversion_per_category'][cat_name] = 0
            for revenue, conversions, category in zip(cls.__dataSet['revenue'], cls.__dataSet['conversions'], cls.__dataSet['category']):
                if cat_name == category:
                    total_revenue['total_revenue_per_category'][cat_name]+= revenue
                    total_conversion['total_conversion_per_category'][cat_name] += conversions

        for type_name in cls.__types:
            total_revenue['total_revenue_per_type'][type_name] = 0
            total_conversion['total_conversion_per_type'][type_name] = 0
            for revenue, conversions, types in zip(cls.__dataSet['revenue'], cls.__dataSet['conversions'], cls.__dataSet['type']):
                if type_name == types:
                    total_revenue['total_revenue_per_type'][type_name] += revenue
                    total_conversion['total_conversion_per_type'][type_name] += conversions


        #print(f"-> The Total revenue per category : {total_revenue['total_revenue_per_category']}")
        #print(f"-> The Total revenue per type : {total_revenue['total_revenue_per_type']}")
        #print(f"-> The Total conversion per category : {total_conversion['total_conversion_per_category']}")
        #print(f"-> The Total conversion per type : {total_conversion['total_conversion_per_type']}")


        for category, type, conversion in zip(cls.__dataSet['category'], cls.__dataSet['type'], cls.__dataSet['conversions']):
            if not (category,type).__str__() in  combinationOfTheMostConvs.keys():
                combinationOfTheMostConvs[(category, type).__str__()] = conversion
            else:
                combinationOfTheMostConvs[(category, type).__str__()] += conversion

        #print(f"->The conversions of category-type combinations : {combinationOfTheMostConvs}") #-> {('FASHION', 'ENGAGEMENT'): 3625, ('FASHION', 'AWARENESS'): 5119, ('ELECTRONICS', 'AWARENESS'): 3782, ('ELECTRONICS', 'CONVERSION'): 3448, ('HOME', 'CONVERSION'): 3829, ('TOYS', 'ENGAGEMENT'): 4199, ('FASHION', 'CONVERSION'): 5271, ('TOYS', 'CONVERSION'): 3323, ('HOME', 'ENGAGEMENT'): 5036, ('ELECTRONICS', 'ENGAGEMENT'): 4952, ('TOYS', 'AWARENESS'): 4025, ('HOME', 'AWARENESS'): 3746}

        top = None

        for i in combinationOfTheMostConvs:
            if combinationOfTheMostConvs[i] == sorted(combinationOfTheMostConvs.values())[-1]:
                top = {i:combinationOfTheMostConvs[i]}

        #print(f"->The category and type combination that generates the most conversions is {top}")


        return {
            'top_performed':top,
            'all_combined_data':combinationOfTheMostConvs
        }

    @classmethod
    def filter_and_aggregate(cls):
        """
        TASK 1 - 4) Filter and Aggregate: Filters rows according to type is CONVERSION. And calculates avg. revenue and conversions for the filtered data.
        """

        filtered_data = []
        avarage_info = {}

        for customer_id, revenue, conversions, typ in zip(cls.__dataSet['customer_id'],cls.__dataSet['revenue'],cls.__dataSet['conversions'],cls.__dataSet['type']):
            if typ == cls.__types[1]:
                filtered_data.append({
                    'customer_id': customer_id,
                    'revenue': revenue,
                    'conversions': conversions,
                    'type': typ
                })


        for id in cls.__customer_id_list:
            total_rev = 0
            total_conv = 0
            count = 0
            for data in filtered_data:
                if data['customer_id'] == id:
                    total_rev += data['revenue']
                    total_conv += data['conversions']
                    count += 1
                    #print(f"->Customer ID: {id}, Revenue: {data['revenue']}, Conversions: {data['conversions']}, Type: {data['type']}, Updated Total Revenue: {total_rev}, Updated Total Conversion: {total_conv}")

            avarage_info[id] = {'avarage_revenue':total_rev/count, 'avarage_conversions':total_conv/count}

        #print(f"\n -> Avarage Revenue and Avarage Conversions Per Customer ID : {avarage_info}")

        return {
            'average': avarage_info,
            'all_aggregated_data': filtered_data
        }





