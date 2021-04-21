FROM openjdk:8u212-b04-jdk-stretch
LABEL author="TonyDC"
LABEL version="0.1"
LABEL source="https://github.com/TonyDC/spark-in-docker"

ENV DAEMON_RUN=true
ENV SPARK_VERSION=3.0.2
ENV HADOOP_VERSION=2.7
ENV SCALA_VERSION=2.12.12
ENV SBT_VERSION=1.4.1
ENV SCALA_HOME=/usr/share/scala
ENV SPARK_HOME=/opt/spark

# Fix the value of PYTHONHASHSEED
# Note: this is needed when you use Python 3.3 or greater
ENV PYTHONHASHSEED 1

WORKDIR /opt/base

COPY ./build ./
COPY ./build-snowflake-jdbc ./
COPY ./build-snowflake-spark ./
COPY ./build-scala ./
COPY ./build-python3 ./
COPY ./build-pyspark ./
COPY ./build-sbt ./
COPY ./build-spark ./

RUN ./build
RUN ./build-snowflake-jdbc
RUN ./build-snowflake-spark
RUN ./build-scala
RUN ./build-python3
RUN ./build-pyspark
RUN ./build-sbt
RUN ./build-spark
