from pyspark.sql import SparkSession
from pyspark.sql.types import Row, StructField, StringType, StructType, FloatType, DataType

# 数据来源
readFileName = "hdfs://master:9000/huadee/save.txt"
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
field1 = StructField("name", StringType(), nullable=True)
field2 = StructField("type", StringType(), nullable=True)
field3 = StructField("box", FloatType(), nullable=True)
fields = [field1, field2, field3]
schema = StructType(fields)

# 获取hdfs上的数据
loan_info = sc.textFile(readFileName)

# 将RDD转换成DF
loan_info_row = loan_info.map(lambda line: line.split('@'))
loan_info_row_rdd = loan_info_row.map(lambda attributes: Row(attributes[0], attributes[5], float(eval(attributes[7]))))
loan_info_df = spark.createDataFrame(loan_info_row_rdd, schema)

# 数据处理
# registerTepTable创建一个临时表
loan_info_df.registerTempTable("mytable")
# 使用sql 语句进行查询
mytabledf = spark.sql("SELECT * from mytable where type='剧情' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='喜剧' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='爱情' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='动作' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='惊悚' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='动画' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='冒险' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='科幻' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='灾难' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='悬疑' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql("SELECT * from mytable where type='文艺' order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1',
                     'append', conn_param)
mytabledf = spark.sql(
    "SELECT * from mytable where type!='剧情' and type!='喜剧' and type!='爱情' and type!='动作' and type!='惊悚' and type!='动画' and type!='冒险' and type!='灾难' and type!='悬疑' and type!='文艺' and type!='科幻'order by box desc limit 9")
mytabledf.write.jdbc("jdbc:mysql://master:3306/huadee?useSSL=false&useUnicode=true&characterEncoding=utf8", 'Rq1_other',
                     'append', conn_param)