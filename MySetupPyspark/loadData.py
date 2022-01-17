import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().getOrCreate()
#spark.sql("use mydb")
df = spark.read.csv('/home/maqsood/Downloads/MOCK_DATA.csv',header=True,inferSchema=True)
df.show(10)
df.printSchema()
df.groupBy('gender').count().show()
df.write.mode("overwrite").saveAsTable("default.test_table1")
df_sql = spark.sql("select * from test_table1")
