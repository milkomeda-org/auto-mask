FROM python:3.6.10
WORKDIR /app
ADD . /app
RUN pip isntall opencv_python-4.2.0.34-cp36-cp36m-manylinux1_x86_64.whl
RUN pip install dlib-19.8.1.tar.gz
RUN pip install -r requirements.txt
EXPOSE 1234
ENV NAME World
CMD ["python","main.py"]