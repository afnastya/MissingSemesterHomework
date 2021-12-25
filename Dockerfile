FROM ubuntu:20.04

WORKDIR /MissingSemesterHomework

RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN pip3 install pyTelegramBotAPI
COPY bot.py .

CMD python3 bot.py