FROM python:3.11-slim-bookworm

COPY ynetd .
COPY flag.txt .
COPY math_server.py .

RUN chmod +x ynetd

EXPOSE 1337

CMD ./ynetd -p 1337 "python3 math_server.py"