FROM alpine:3.10

RUN apk update
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN apk add nfs-utils

WORKDIR /app

COPY requirements.txt /app
COPY app.py /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "app.py"]
