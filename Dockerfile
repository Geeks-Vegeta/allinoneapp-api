FROM python:3.7.6-alpine
RUN python -m pip install --upgrade pip
WORKDIR /app
# Install native libraries, required for numpy
RUN apk --no-cache add musl-dev linux-headers g++
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow zbar
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]