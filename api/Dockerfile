FROM python:alpine
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py