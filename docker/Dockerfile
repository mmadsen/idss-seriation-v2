FROM python:3.7-slim

MAINTAINER mark@ibisnetworks.com

RUN \
  DEBIAN_FRONTEND=noninteractive \
    apt update && apt install --assume-yes --no-install-recommends \
      build-essential \
      nasm \
      vim-common \
      curl \
      wget \
      git \
  \
  && rm -rf /var/lib/apt/lists/*

ENV APPDIR=/app/
RUN mkdir $APPDIR

COPY ./service/production/main.py $APPDIR/main.py
COPY asset_utilization_service $APPDIR/asset_utilization_service
COPY cacert.pem $APPDIR/cacert.pem
COPY requirements.txt $APPDIR/requirements.txt

WORKDIR $APPDIR
RUN pip install -r requirements.txt

RUN \
  DEBIAN_FRONTEND=noninteractive \
    apt update && apt remove --purge --assume-yes --no-install-recommends \
      build-essential \
      nasm \
      vim-common \
      curl \
      wget \
      git \
  \
  && rm -rf /var/lib/apt/lists/*

CMD ["python", "./main.py"]
