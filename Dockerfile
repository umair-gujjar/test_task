FROM ubuntu:latest
MAINTAINER Muhhammad Umair Sabir "engrumair_sabir@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python-mysqldb
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]
