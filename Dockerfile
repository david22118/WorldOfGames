FROM python:alpine3.13
WORKDIR /app
COPY requirements.txt ./
COPY Utils.py ./
COPY MainScores.py ./
COPY scores.txt ./
EXPOSE 8777
RUN pip install -r requirements.txt
CMD [ "python","MainScores.py"]