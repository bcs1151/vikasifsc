FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD web: waitress-serve --port=$PORT shivalik.wsgi:application