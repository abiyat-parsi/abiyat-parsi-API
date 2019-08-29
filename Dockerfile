FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD db.sqlite3 /mnt/shared-volume/
ADD . /code/
ENTRYPOINT ["sh","/code/run.sh"]