FROM python:alpine3.13
WORKDIR /app
COPY Utils.py ./
COPY MainScores.py ./
COPY scores.txt ./
EXPOSE 8777
RUN pip install Flask
CMD ["python" , "MainScores.py"]
