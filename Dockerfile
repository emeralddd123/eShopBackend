FROM python:3.11

RUN mkdir '/home/app'

ADD ./app ./home/app

#RUN pip cache purge

RUN pip install -r "/home/app/requirements.txt"

RUN ["python", "/home/app/manage.py", "makemigrations"]

RUN ["python", "/home/app/manage.py", "migrate"]

CMD [ "python", "/home/app/manage.py",  "runserver", "0.0.0.0:8000"]