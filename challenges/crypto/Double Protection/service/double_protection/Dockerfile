FROM python:3-onbuild

RUN pip install -r requirements.txt

WORKDIR /application
COPY * /application/

CMD ["python","app.py"]
EXPOSE 1337