# Retail Sales Analysis with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, month, year
import matplotlib.pyplot as plt
import seaborn as sns

# Create Spark session
spark = SparkSession.builder.appName("RetailSalesAnalysis").getOrCreate()

# Load dataset (replace with your local path)
df = spark.read.csv("<your_dataset_file_path>", header=True, inferSchema=True)

# Preview data
df.show(5)
df.printSchema()

# Data Cleaning
df_cleaned = df.dropDuplicates().na.drop()

# Optional: convert date column if available (adjust column name accordingly)
# df_cleaned = df_cleaned.withColumn("Date", to_date(col("Date"), "MM/dd/yyyy"))

# Create temporary view for Spark SQL
df_cleaned.createOrReplaceTempView("sales")

# Aggregations
sales_per_product = spark.sql("""
    SELECT `Product Category`, SUM(`Total Amount`) AS TotalSales
    FROM sales
    GROUP BY `Product Category`
""")

sales_per_store = spark.sql("""
    SELECT `Store ID`, SUM(`Total Amount`) AS TotalSales
    FROM sales
    GROUP BY `Store ID`
""")

sales_per_customer = spark.sql("""
    SELECT `Customer ID`, SUM(`Total Amount`) AS TotalSales
    FROM sales
    GROUP BY `Customer ID`
""")

# Convert to Pandas for Visualization
top_products_pd = sales_per_product.orderBy(col("TotalSales").desc()).toPandas()
top_stores_pd = sales_per_store.orderBy(col("TotalSales").desc()).toPandas()
top_customers_pd = sales_per_customer.orderBy(col("TotalSales").desc()).toPandas()

# Visualization: Top Products
plt.figure(figsize=(10, 6))
sns.barplot(x='Product Category', y='TotalSales', data=top_products_pd)
plt.title('Top Selling Product Categories')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization: Top Stores
plt.figure(figsize=(10, 6))
sns.barplot(x='Store ID', y='TotalSales', data=top_stores_pd)
plt.title('Top Performing Stores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization: Top Customers
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer ID', y='TotalSales', data=top_customers_pd.head(10))
plt.title('Top 10 Valuable Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# df_cleaned.cache()
# df_cleaned = df_cleaned.repartition("Store ID")
