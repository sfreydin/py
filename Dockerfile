FROM python:alpine3.7
ARG TAG
ENV TAG=${TAG}
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./app.py