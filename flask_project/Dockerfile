FROM python:3.10

RUN apt-get upgrade & apt update

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5001" ]
