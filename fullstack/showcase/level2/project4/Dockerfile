FROM python:3
COPY . /usr/src/networkcs50
WORKDIR /usr/src/networkcs50
RUN pip install -r requirements.txt
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
