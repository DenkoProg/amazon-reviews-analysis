from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName("PySparkTest").getOrCreate()
    data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
    columns = ["id", "name"]
    df = spark.createDataFrame(data, columns)
    df.show()
    spark.stop()
