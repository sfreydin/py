FROM python:alpine3.7
ARG IMAGE_TAG
ENV IMAGE_TAG=${IMAGE_TAG}
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --timeout 100
EXPOSE 8080
CMD python ./app.py