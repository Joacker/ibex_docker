FROM ubuntu:latest


RUN apt-get update && apt-get install -y \
    bash \
    g++ \
    gcc \
    flex \
    bison \
    python2-dev \
    make \
    build-essential \
    libeigen3-dev

RUN apt install -y \
    python-is-python3
#RUN apk add --update alpine-sdk

RUN cd /usr/local/include \
&& ln -s /usr/include/eigen3/Eigen Eigen \
&& ln -s /usr/include/eigen3/unsupported unsupported

WORKDIR /app

COPY ./ibex-lib-master /app
#RUN ./waf configure --interval-lib=gaol --lp-lib=soplex  --with-optim \
#&& ./waf

# ./__build__/src/ibexopt benchs/optim/medium/alkylbis.bch --random-seed=1

# Mantener el contenedor en ejecución
CMD ["tail", "-f", "/dev/null"]