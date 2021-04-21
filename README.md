# Spark in Docker

Create a Apache Spark cluster in Docker.

Note that this is just a proof of concept I developed just for testing purposes. See the Sources section for more information about the places I checked out. Moreover, some cleanup activities and enhancements are required, which I will try to do in my spare time.

## Commands

**Build images (with base)**:

```shell
DEPLOY_BASE=1 ./build
```

**Build images (reusing base image)**:

```shell
./build
```

**Start cluster**:

```shell
docker-compose up --scale spark-master=1 --scale spark-worker=6 --scale spark-submit=0
```

**Submit task**:

```shell
docker-compose run spark-submit
./run <script args>
```

## Sources

- <https://github.com/mvillarrealb/docker-spark-cluster>
