FROM ubuntu:latest
RUN apt-get update
RUN apt update
RUN apt-get install python3 -y
WORKDIR /usr/app/src

COPY study_timer.py ./
CMD [ "python3", "./study_timer.py"]
