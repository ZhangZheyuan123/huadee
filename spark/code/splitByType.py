from pyspark.sql import SparkSession

# 数据来源文件位置
readFileName = "hdfs://master:9000/huadee/all.txt"
# 拆分后数据存放位置
outPutFilename = "hdfs://master:9000/huadee/save.txt"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext

# 获取hdfs上的数据
loan_info = sc.textFile(readFileName)


# 拆分方法
def SplitByType(line):
    attributes = line.split('@')
    rets = []
    countOfType = int(len(attributes[5]) / 2)
    while (countOfType != 0):
        ret = attributes[0] + "@" + attributes[1] + "@" + attributes[2] + "@" + attributes[3] + "@" + attributes[
            4] + "@" + \
              attributes[5][countOfType * 2 - 2:countOfType * 2] + "@" + attributes[6] + "@" + attributes[7] + "@" + \
              attributes[8]
        countOfType = countOfType - 1
        rets.append(ret)
        pass
    return rets
    pass


# 拆分且存储
lines = loan_info.flatMap(lambda line: SplitByType(line))
lines.saveAsTextFile(outPutFilename)