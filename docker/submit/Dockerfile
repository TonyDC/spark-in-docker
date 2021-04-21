FROM tonydc/spark-base:2.4.7

WORKDIR /opt/submit
COPY ./run ./

ENV SPARK_MASTER_URL="spark://spark-master:7077"
ENV SPARK_SUBMIT_ARGS=""
ENV SPARK_APPLICATION_ARGS=""

# CMD ["/bin/bash", "/opt/submit/run"]
