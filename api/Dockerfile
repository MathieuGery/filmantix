FROM python:3.9

WORKDIR /app
ENV TZ=Europe/Paris
COPY api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./api .

CMD [ "python3", "-u", "app.py"]