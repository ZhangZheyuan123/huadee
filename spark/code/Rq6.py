from pyspark.sql import SparkSession
from pyspark.sql.types import Row, StructField, StringType, StructType, FloatType, DataType

# 数据来源
readFileName = "hdfs://master:9000/huadee/all.txt"
# 输出方向:数据库
conn_param = {}
conn_param['user'] = 'root'
conn_param['password'] = 'z123456'
conn_param['driver'] = "com.mysql.jdbc.Driver"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext

# 构建数据的属性schema
field1 = StructField("area", StringType(), nullable=True)
fields = [field1]
schema = StructType(fields)

# 获取hdfs上的数据
loan_info = sc.textFile(readFileName)

# 将RDD转换成DF
loan_info_row = loan_info.map(lambda line: line.split('@'))
loan_info_row_rdd = loan_info_row.map(lambda attributes: Row(attributes[2]))
loan_info_df = spark.createDataFrame(loan_info_row_rdd, schema)

# 数据处理
result_df = loan_info_df.groupBy("area").count()

# 写入数据库
result_df.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq6',
                     'append', conn_param)
