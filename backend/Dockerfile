FROM 3.12.1-bookworm

RUN mkdir /backend
ADD requirements.txt /backend

ENV PYTHONUNBUFFERED 1
EXPOSE 5000

WORKDIR /backend
RUN pip3 install -r requirements.txt
