FROM python:3.7.6-alpine
RUN python -m pip install --upgrade pip
WORKDIR /app
# Install native libraries, required for numpy
RUN apk --no-cache add musl-dev linux-headers g++
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
RUn wget http://dl-cdn.alpinelinux.org/alpine/v3.14/community/aarch64/zbar-dev-0.23.90-r1.apk && apk add zbar-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE $PORT
CMD ["python", "app.py"]
