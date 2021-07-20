FROM python:3.9-buster

WORKDIR /app

ENV FLASK_ENV=development

COPY ./requirements.txt requirements.txt

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD flask run --host=0.0.0.0