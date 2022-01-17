import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().getOrCreate()
#read json from text file
dfFromTxt=spark.read.text("/home/maqsood/Downloads/data2.txt")
dfFromTxt.printSchema()
# Create Schema of the JSON column
from pyspark.sql.types import StructType,StructField, StringType
schema = StructType([
	StructField('id',StringType(),True), 
    	StructField('venue',StringType(),True), 
    	
	StructField('result',StringType(),True)
  ])
#Convert json column to multiple columns
from pyspark.sql.functions import col,from_json
dfJSON = dfFromTxt.withColumn("jsonData",from_json(col("value"),schema)) \
                   .select("jsonData.*")
dfJSON.printSchema()
dfJSON.show(truncate=False)
#dfJSON.write.mode("overwrite").saveAsTable("test_table2")
#df_sql=spark.sql("select * from test_table2")
