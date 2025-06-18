# Problem 1 : Group Sold Products by the Date	(https://leetcode.com/problems/group-sold-products-by-the-date/)

import pandas as pd

# solution 1: using a for loop
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    dict = {}
    for i in range(len(activities)):
        s_date = activities['sell_date'][i]
        pdt = activities['product'][i]
        if s_date not in dict:
            dict[s_date] = set()
        dict[s_date].add(pdt)
    result = []
    for key, value in dict.items():
        temp = [p for p in value]
        temp.sort()
        # temp = sorted(value)  # this would also work and sorted returns a list
        s = ','.join(temp)
        result.append([key, len(value), s])

    return pd.DataFrame(result, columns=['sell_date', 'num_sold', 'products']).sort_values('sell_date')

# solution 2: using pandas functions
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date').agg(
        num_sold = ('product', 'nunique'),
        products = ('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    return df.sort_values('sell_date')


"""
- 'nunique', 'count', 'sum' etc. are Pandas-specific string method names, so they must be in quotes.
- min, max, len, etc. are built-in Python functions, so they can be used with or without quotes, depending on context.
- reset_index() would return my column back and 0,1,2... becaomes a new index.

- if we mention a single column in the agg or any other function, then we get back series. 
if we use the full df then, df is returned

eg: df = activities.groupby('sell_date')['product'].agg(max) -> this returns a series with index as sell_date and values as max of product
    df = activities.groupby('sell_date').agg(max) -> this returns a df

    df = activities.groupby('sell_date')['product']max() -> series
    df = activities.groupby('sell_date').max() -> df
"""