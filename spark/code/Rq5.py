from pyspark.sql import SparkSession
from pyspark.sql.types import Row, StructField, StringType, IntegerType, StructType

# 数据来源
readFileName = "hdfs://master:9000/huadee/all.txt"
# 输出方向:数据库
conn_param = {}
conn_param['user'] = 'root'
conn_param['password'] = 'z123456'
conn_param['driver'] = "com.mysql.jdbc.Driver"
# 好烂片划分分数
scoreToDivideNiceOrShit = 7.0

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext

# 构建数据的属性schema
field1 = StructField("year", StringType(), nullable=True)
field2 = StructField("nice", IntegerType(), nullable=True)
field3 = StructField("shit", IntegerType(), nullable=True)
fields = [field1, field2, field3]
schema = StructType(fields)

# 获取hdfs上的数据
loan_info = sc.textFile(readFileName)


# 将RDD转换成DF
def DivideNiceOrShit(attributes):
    score = float(attributes[6])
    if score > scoreToDivideNiceOrShit or score == scoreToDivideNiceOrShit:
        return Row(attributes[1], 1, 0)
        pass
    elif score < scoreToDivideNiceOrShit and score != 0:
        return Row(attributes[1], 0, 1)
        pass
    else:
        return Row(attributes[1], 0, 0)


loan_info_row = loan_info.map(lambda line: line.split('@'))
loan_info_row_rdd = loan_info_row.map(lambda attributes: DivideNiceOrShit(attributes))
loan_info_df = spark.createDataFrame(loan_info_row_rdd, schema)

# 数据处理
# GroupedData是GROUPBY函数返回的类型，mean函数可以求平均值，此时列名为 type和avg(box)
# sum可以用于求总值，此时列名为type和sum(box)
loan_info_df.registerTempTable("mytable")
mytabledf = spark.sql("SELECT * from mytable where year<2020 and year>2012")
result_df = mytabledf.groupBy("year").sum()

# 写入数据库
result_df.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8",
                     'Rq5', 'append', conn_param)
