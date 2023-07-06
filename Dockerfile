FROM python:3.10-slim-buster
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-pip git \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

RUN mkdir /Insta-DL
WORKDIR /Insta-DL
#RUN apt update && apt upgrade -y && apt install ffmpeg python3 python3-pip apt-utils -y
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]
