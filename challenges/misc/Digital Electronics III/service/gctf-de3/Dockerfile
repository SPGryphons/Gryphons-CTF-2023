FROM python
WORKDIR /app
COPY . .
RUN chmod +x server/get_pio.sh
RUN ./server/get_pio.sh

RUN chmod +x server/get_wokwi.sh
RUN ./server/get_wokwi.sh

ENV WOKWI_CLI_TOKEN wok_zOhEhKuWCyuQ1b8iBbBytNnSujNQEwpl8ad228df


RUN pip3 install flask
# NOTE: THIS IS INSECURE! TO BE CHANGED TO GUNICORN WSGI INSTEAD!
WORKDIR /app/server
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
