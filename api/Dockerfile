# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
CMD uvicorn main:app --reload --host 0.0.0.0
