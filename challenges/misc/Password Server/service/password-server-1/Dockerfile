FROM python:3.11-slim-bookworm

COPY ynetd .
COPY flag.txt .
COPY main.py .

RUN chmod +x ynetd

EXPOSE 1337

CMD ./ynetd -p 1337 "python3 main.py"