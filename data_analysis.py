import pandas as pd

QVI_PATH = "QVI_data.csv"
QVI_DF = pd.read_csv(QVI_PATH)

store_numbers = QVI_DF.STORE_NBR.unique()
unique_customers = QVI_DF.LYLTY_CARD_NBR.unique()

#dataframe of total sales revenue from each store 
QVI_by_sales_and_customers = QVI_DF.groupby(["STORE_NBR"]).agg(SUM_SALES = ("TOT_SALES", "sum"), NUM_CUSTOMERS = ("LYLTY_CARD_NBR", "count"))
print(QVI_by_sales_and_customers)

#dataframe for number of transactions for each customer
QVI_by_prod_qty = QVI_DF.groupby("LYLTY_CARD_NBR")["PROD_QTY"].sum()
print(QVI_by_prod_qty)

#average number of transactions per customer
print(QVI_by_prod_qty.mean())

#CONTROL STORES: 211, 226
minValueIndexObj = QVI_by_sales_and_customers.idxmin()
maxValueIndexObj = QVI_by_sales_and_customers.idxmax()

#find the min and max sales
min_sales = QVI_by_sales_and_customers["SUM_SALES"].min()
max_sales = QVI_by_sales_and_customers["SUM_SALES"].max()

#Use Pearson correlations as a measure:
#1- (Observed distance – minimum distance)/(Maximum distance – minimum distance)  

#pearson correlations for trial store 77
pearson_correlations_77 = 1 - (3040.00 - min_sales) / (max_sales - min_sales)

#pearson correlations for trial store 86
pearson_correlations_86 = 1 - (10635.35 - min_sales) / (max_sales - min_sales)

#pearson correlations for trial store 88
pearson_correlations_88 = 1 - (16333.25 - min_sales) / (max_sales - min_sales)






