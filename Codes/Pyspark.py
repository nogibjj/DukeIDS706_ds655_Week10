import urllib.request
from pyspark.sql import SparkSession
from pyspark import SparkFiles

# Download the file
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz"
filename = "HIGGS.csv.gz"
urllib.request.urlretrieve(url, filename)

spark = SparkSession.builder.appName("UCI ML Repo data processing").getOrCreate()
spark.sparkContext.addFile(url)

df = spark.read.csv(SparkFiles.get("HIGGS.csv.gz"), header=True, inferSchema=True)

# filtered_data = df.select("column_name").filter(df["column_name"] > 100)

count = df.count()

print("Number of rows in the dataset: ", count)
# filtered_data.write.csv('s3a://bucket_name/path_to_save_file.csv')
spark.stop()
# os.remove("HIGGS.csv.gz")
