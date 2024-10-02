FROM python:3
WORKDIR /bot

RUN apt-get update -qq && apt-get install ffmpeg libsm6 libxext6 -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /video
RUN mkdir /frames
RUN mkdir /input

CMD ["python","-u", "main.py"]