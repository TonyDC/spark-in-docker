import logging
import sys

from py4j.java_gateway import java_import
from pyspark import SparkConf, sql

# Create logger
logging.basicConfig(format='%(asctime)-15s %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger()

# Set Spark configuration

# Note: a configuration called `setMaster` is available. According to the documentation,
# if its value is set to `local`, single thread of a single machine will be used. If not
# set, the default value will be used (I assume it's the entire cluster)
# Source: https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkConf.html
# #setMaster-java.lang.String-
conf = SparkConf().setAppName('Data ingestion')

# Apache Spark Session vs Context
# TL;DR: allows different users to use the same context by using different sessions
# Source: https://medium.com/@achilleus/spark-session-10d0d66d1d24
spark = sql.SparkSession.builder \
    .config(conf=conf) \
    .getOrCreate()

spark.sparkContext.setLogLevel("INFO")

# Spark snowflake plugin configuration
# Source: https://docs.snowflake.com/en/user-guide/spark-connector-use.html
java_import(spark._jvm, "net.snowflake.spark.snowflake")

spark._jvm \
    .net.snowflake.spark.snowflake.SnowflakeConnectorUtils \
    .enablePushdownSession(spark._jvm.org.apache.spark.sql.SparkSession.builder().getOrCreate())

if __name__ == '__main__':
    data_lake = sys.argv[1]
    data_warehouse = sys.argv[2]
    channel = sys.argv[3]

    try:
        res = handler(spark=spark,
                      data_lake=data_lake,
                      data_warehouse=data_warehouse,
                      channel=channel)
        logger.info(f'Handler result: {res}')
    except Exception:
        logger.exception('Ingestion failed')
        raise
    finally:
        spark.stop()

    logger.info('Execution finished')
