FROM centos:7
# Install Python 3.6
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python36u && \
    yum -y install python36u-pip && \
    yum -y install vim && \
    yum clean all  &&  rm -rf /var/cache/yum

RUN pip3.6 --no-cache-dir install -r requirements.txt \
        && \
    python3.6 -m ipykernel.kernelspec
# Install opencv-python
RUN yum -y install libSM-1.2.2-2.el7.x86_64 --setopt=protected_multilib=false  && \
    yum install ksh -y  && \
    yum install libXext.so.6 -y  && \
    yum install libXtst.so.6 -y  && \
    yum install libXt.so.6 -y  && \
    yum install libGLU.so.1 --setopt=protected_multilib=false -y  && \
    yum install libelf.so.1 -y  && \
    yum install libXrender.so.1 -y  && \
    yum install libXp.so.6 -y  && \
    yum install libXrandr.so.2 -y  && \
    yum install *xorg* -y --skip-broken  && \
    yum install libXp -y  && \
    yum install ld-linux.so.2 -y  && \
    yum install openmotif -y  && \
    yum install libstdc++.so.5 -y  && \
    yum install xterm -y  && \
    yum clean all  &&  rm -rf /var/cache/yum

RUN pip3.6 --no-cache-dir install opencv-python==3.4.1.15

# Install dlib
RUN yum -y groupinstall "Development tools"  && \
    yum -y install cmake && \
    yum install -y boost boost-devel boost-doc  && \
    yum install -y libXdmcp libXdmcp-devel  && \
    yum clean all  &&  rm -rf /var/cache/yum

RUN yum search python3 | grep devel  && \
    yum install -y python36u-devel.x86_64  && \
    yum clean all  # &&  rm -rf /var/cache/yum

RUN pip3.6 --no-cache-dir install dlib

WORKDIR /app
ADD . /app
EXPOSE 1234
ENV NAME DEV
CMD ["python","main.py"]