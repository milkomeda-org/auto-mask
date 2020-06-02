FROM python:3.6.10
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 1234
ENV NAME World
CMD ["python","main.py"]