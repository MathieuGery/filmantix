FROM python:3.9-slim

WORKDIR /app
ENV TZ=Europe/Paris
COPY api/requirements.txt requirements.txt
RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev
RUN pip3 install -r requirements.txt
RUN python -m spacy download fr_core_news_lg
COPY ./api .

CMD [ "python3", "-u", "app.py"]