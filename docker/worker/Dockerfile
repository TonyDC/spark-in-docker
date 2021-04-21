FROM tonydc/spark-base:2.4.7

WORKDIR /opt/worker
COPY ./start ./

ENV SPARK_WORKER_WEBUI_PORT=8081
ENV SPARK_WORKER_LOG="/opt/logs"
ENV SPARK_MASTER="spark://spark-master:7077"

EXPOSE 8081

CMD ["/bin/bash", "/opt/worker/start"]
