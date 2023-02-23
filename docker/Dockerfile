# Author Ignacio Lizarán
FROM ubuntu:22.04

ENV LANG es_ES.UTF-8

RUN DEBIAN_FRONTEND=noninteractive TZ=Europe/Madrid apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        dirmngr \
        fonts-noto-cjk \
        gnupg \
        libssl-dev \
        vim \
        git \
        python3 \
        python3-pip \
        build-essential \
        python3-dev \
        python3-venv \
        python3-wheel \
        libxslt-dev \
        libzip-dev \
        python3-setuptools \
        node-less \
        libjpeg-dev \
        zlib1g-dev \
        gdebi \
        python3-pil \
        libpq-dev \
        nginx \
        supervisor \
        libxml2-dev \
        libxslt1-dev \
        libjpeg8 \
        libjpeg8-dev \ 
        libfreetype6 \
        libfreetype6-dev \
        xz-utils \
        gettext \
        net-tools \
        iputils-ping \
        libmysqlclient-dev \
        language-pack-es-base 

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir uwsgi


COPY requirements.txt /code/
RUN pip3 install --no-cache-dir -r /code/requirements.txt

COPY . /code/

WORKDIR /code/


RUN cp docker/nginx.conf /etc/nginx/nginx.conf
RUN cp docker/supervisord.conf /etc/supervisor/conf.d/

# django static
RUN python3 manage.py collectstatic --noinput

CMD ["supervisord"]
