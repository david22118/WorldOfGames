FROM python:alpine3.13
WORKDIR /app
RUN pip install Flask
COPY Utils.py ./
COPY MainScores.py ./
COPY Scores.txt ./
EXPOSE 8777
CMD ["python3" , "MainScores.py"]
