FROM digi0ps/python-opencv:latest
MAINTAINER vinson
RUN CPUCORES=$(getconf _NPROCESSORS_ONLN)

# Essential packages
RUN apt update && apt install -y build-essential cmake pkg-config \
    libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev \
    && pip install numpy


# Compile Dlib using cmake
RUN mkdir -p ~/dlib \
    && cd ~/dlib \
    && wget http://dlib.net/files/dlib-19.16.tar.bz2 \
    && tar xf dlib-19.16.tar.bz2 \
    && cd ~/dlib/dlib-19.16 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && cmake --build . --config Release \
    && make -j${CPUCORES} \
    && cd ~/dlib/dlib-19.16/build \
    && make install \
    && ldconfig

# Install packages for Python
RUN pkg-config --libs --cflags dlib-1 \
    && cd ~/dlib/dlib-19.16 \
    && python setup.py install \
    && rm -rf ~/dlib /var/cache/apk/* /usr/share/man /usr/local/share/man /tmp/*
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 1234
ENV NAME World
CMD ["python","main.py"]