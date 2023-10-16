FROM debian:stable

COPY flag.txt .
COPY noteinator .
COPY ynetd .

RUN chmod +x ynetd
RUN chmod +x noteinator

EXPOSE 1337

CMD ./ynetd -p 1337 ./noteinator
