FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install Flask
COPY Utils.py ./
COPY MainScores.py ./
COPY Scores.txt ./
EXPOSE 8777
CMD ["python3" , "MainScores.py"]
