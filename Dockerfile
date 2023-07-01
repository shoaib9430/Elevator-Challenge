FROM python:3.9.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /www/app

COPY requirements.txt ./

RUN pip install virtualenv

RUN virtualenv venv

RUN . venv/bin/activate

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]