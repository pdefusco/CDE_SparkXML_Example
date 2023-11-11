from pyspark.sql import SparkSession
import cml.data_v1 as cmldata
from pyspark import SparkContext
import pyspark.sql.functions as F
from pyspark.sql.functions import col

spark = SparkSession \
        .builder \
        .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")\
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")\
        .config("spark.jars.packages","com.databricks:spark-xml_2.12:0.16.0")\
        .appName("Isilon Decode XML Pull") \
        .getOrCreate()

df = spark.read.format('xml').options(rowTag='TopAttribute').load('sample_iot.xml')

df.show()

df.printSchema()

df.select("metrics.myMetrics.name").show()

def flatten_df(nested_df):
    stack = [((), nested_df)]
    columns = []
    while len(stack) > 0:
        parents, df = stack.pop()
        for column_name, column_type in df.dtypes:
            if column_type[:6] == "struct":
                projected_df = df.select(column_name + ".*")
                stack.append((parents + (column_name,), projected_df))
            else:
                columns.append(col(".".join(parents + (column_name,))).alias("_".join(parents + (column_name,))))
    return nested_df.select(columns)
  
flatten_df(df).show()

flatten_df(df).printSchema()