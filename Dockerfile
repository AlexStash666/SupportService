FROM python:3.10

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN apt install -y netcat

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY . .

CMD ["sh","./entrypoint.sh"]