FROM bde2020/spark-base:1.5.1-hadoop2.6

MAINTAINER Erika Pauwels <erika.pauwels@tenforce.com>

RUN apt-get update && apt-get install -y python

COPY runSparkSubmitCommand.py runSparkSubmitCommand.py

ENTRYPOINT ["python", "runSparkSubmitCommand.py"]

CMD ["application.jar"]
