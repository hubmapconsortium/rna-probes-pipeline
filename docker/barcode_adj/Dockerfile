FROM pypy:3.8

## System packages
RUN apt-get update \
 && apt-get -y install --no-install-recommends \
    samtools \
 && rm -rf /var/cache/apt/* /var/lib/apt/lists/*

## Python packages
COPY docker/barcode_adj/requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt \
 && rm -rf /root/.cache/pip

COPY bin/common /opt
COPY bin/analysis /opt

WORKDIR /opt

RUN wget https://hubmap-pipeline-assets.s3.amazonaws.com/salmon/737K-fixed-rna-profiling.txt
