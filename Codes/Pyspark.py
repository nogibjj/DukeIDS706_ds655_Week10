from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("common_crawl_processing").getOrCreate()

# Replace 's3a://commoncrawl/crawl-data/CC-MAIN-2022-01/segments/1640203805123.60/warc/' with the actual path to the dataset you want to use
df = spark.read.format("com.databricks.spark.warc").load(
    "s3a://commoncrawl/crawl-data/CC-MAIN-2022-01/segments/1640203805123.60/warc/"
)

# Replace 'column_name' with the actual column name you're interested in
filtered_data = df.select("column_name").filter(df["column_name"] > 100)

count = df.count()

print(count)
# Replace 's3a://bucket_name/path_to_save_file.csv' with the actual S3 path where you want to save the processed data
# filtered_data.write.csv('s3a://bucket_name/path_to_save_file.csv')
