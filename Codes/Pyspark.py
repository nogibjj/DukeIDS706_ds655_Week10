import urllib.request
import os
from pyspark.sql import SparkSession

# Download the file
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz"
filename = "HIGGS.csv.gz"
urllib.request.urlretrieve(url, filename)

spark = SparkSession.builder.appName("UCI ML Repo data processing").getOrCreate()

# Replace 's3a://commoncrawl/crawl-data/CC-MAIN-2022-01/segments/1640203805123.60/warc/' with the actual path to the dataset you want to use
df = spark.read.csv(filename, header=True, inferSchema=True)

# Replace 'column_name' with the actual column name you're interested in
# filtered_data = df.select("column_name").filter(df["column_name"] > 100)

count = df.count()

print(count)
# Replace 's3a://bucket_name/path_to_save_file.csv' with the actual S3 path where you want to save the processed data
# filtered_data.write.csv('s3a://bucket_name/path_to_save_file.csv')
spark.stop()
os.remove("HIGGS.csv.gz")
