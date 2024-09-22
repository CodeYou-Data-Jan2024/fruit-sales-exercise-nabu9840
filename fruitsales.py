import pandas as pd
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [25,34]}, index=['2017 sales', '2018 sales'])
fruit_sales.to_csv('fruit.csv', index=False)