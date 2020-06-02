FROM centos:7
MAINTAINER vinson
# Install Python
RUN set -ex \
    # 预安装所需组件
    && yum install -y wget tar libffi-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make gcc-c++ initscripts \
    && wget https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz \
    && tar -zxvf Python-3.6.10.tgz \
    && cd Python-3.6.10 \
    && ./configure prefix=/usr/local/python3 \
    && make \
    && make install \
    && make clean \
    && rm -rf /Python-3.6.10* \
    && yum install -y epel-release \
    && yum install -y python-pip \
# 设置默认为python3
    # 备份旧版本python
    && mv /usr/bin/python /usr/bin/python27 \
    && mv /usr/bin/pip /usr/bin/pip-python27 \
    # 配置默认为python3
    && ln -s /usr/local/python3/bin/python3.6 /usr/bin/python \
    && ln -s /usr/local/python3/bin/pip3 /usr/bin/pip \
# 修复因修改python版本导致yum失效问题
    && sed -i "s#/usr/bin/python#/usr/bin/python27#" /usr/bin/yum \
    && sed -i "s#/usr/bin/python#/usr/bin/python27#" /usr/libexec/urlgrabber-ext-down \
    && yum install -y deltarpm \
# 基础环境配置
    # 修改系统时区为东八区
    && rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && yum install -y vim \
    # 安装定时任务组件
    && yum -y install cronie \
# 支持中文
    && yum install kde-l10n-Chinese -y \
    && localedef -c -f UTF-8 -i zh_CN zh_CN.utf8 \
# 更新pip版本 安装pip包
    && pip install --upgrade pip \
    && pip install pyltp -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
ENV LC_ALL zh_CN.UTF-8

RUN pip --no-cache-dir install -r requirements.txt \
        && \
    python -m ipykernel.kernelspec
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

RUN pip --no-cache-dir install opencv-python==3.4.1.15

# Install dlib
RUN yum -y groupinstall "Development tools"  && \
    yum -y install cmake && \
    yum install -y boost boost-devel boost-doc  && \
    yum install -y libXdmcp libXdmcp-devel  && \
    yum clean all  &&  rm -rf /var/cache/yum

RUN yum search python3 | grep devel  && \
    yum install -y python36u-devel.x86_64  && \
    yum clean all  # &&  rm -rf /var/cache/yum

RUN pip --no-cache-dir install dlib

WORKDIR /app
ADD . /app
EXPOSE 1234
ENV NAME DEV
CMD ["python","main.py"]