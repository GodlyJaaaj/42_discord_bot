FROM python:latest

WORKDIR /app/discord_bots/42_bot
COPY . .
RUN ["pip3", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python3", "main.py"]

