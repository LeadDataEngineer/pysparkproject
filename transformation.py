# added a sample transformation using PySpark
# transformation.py
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SampleTransformation") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 34),
    ("Bob", 45),
    ("Cathy", 29)
]

# Create DataFrame
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Transformation: filter rows where Age > 30
filtered_df = df.filter(df.Age > 30)

# Show results
filtered_df.show()

# Stop Spark session
spark.stop()