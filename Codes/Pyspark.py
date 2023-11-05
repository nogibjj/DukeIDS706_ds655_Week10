import pandas as pd
from pyspark.sql import SparkSession
import io
import requests
import gzip

# URL of the file to download
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz"

# Create a SparkSession
spark = SparkSession.builder.appName("UCI ML Repo data processing").getOrCreate()

# Download the file and decompress it
r = requests.get(url)
gz = gzip.open(io.BytesIO(r.content))
df_pd = pd.read_csv(gz)

# Convert the pandas DataFrame to a PySpark DataFrame
df = spark.createDataFrame(df_pd)

# Count the number of rows in the DataFrame
count = df.count()

print("Number of rows in the dataset: ", count)

# Stop the SparkSession
spark.stop()
