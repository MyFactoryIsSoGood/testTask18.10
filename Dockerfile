FROM python:3.10

COPY meta solution/meta

RUN pip install -r solution/meta/requirements.txt --no-cache-dir --upgrade

EXPOSE 8000

WORKDIR /solution/