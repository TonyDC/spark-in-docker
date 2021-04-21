FROM spark-base:2.4.7

WORKDIR /opt/master
COPY ./start ./

ENV SPARK_MASTER_PORT=7077
ENV SPARK_MASTER_WEBUI_PORT=8080
ENV SPARK_MASTER_LOG="/opt/logs"

EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/opt/master/start"]
