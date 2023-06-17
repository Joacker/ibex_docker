FROM alpine:3.13.5

RUN apk update && apk add --no-cache \
    bash \
    g++ \
    gcc \
    flex \
    bison \
    python2 \
    make \
    wget \
    cmake \
    curl \
    git \
    build-base \
    openjdk8 
# Clone the Eigen repository
RUN git clone https://github.com/eigenteam/eigen-git-mirror.git /usr/src/eigen

# Build and install Eigen
RUN mkdir /usr/src/eigen/build && \
    cd /usr/src/eigen/build && \
    cmake .. && \
    make install

# ./waf distclean

# Cleanup
RUN rm -rf /usr/src/eigen

RUN apk add --update alpine-sdk

# Continue with your Dockerfile instructions
WORKDIR /app
COPY ./ibex-lib-master /app

CMD ["tail", "-f", "/dev/null"]

# FROM ubuntu:latest


# RUN apt-get update && apt-get install -y \
#     bash \
#     g++ \
#     gcc \
#     flex \
#     bison \
#     python2-dev \
#     make \
#     build-essential 

# RUN apt install -y \
#     python-is-python3
# #RUN apk add --update alpine-sdk

# WORKDIR /app

# COPY ./ibex-lib-master /app
# #RUN ./waf configure --interval-lib=gaol --lp-lib=soplex \
# #&& 

# # ./__build__/src/ibexopt benchs/optim/medium/alkylbis.bch --random-seed=1

# # Mantener el contenedor en ejecución
# CMD ["tail", "-f", "/dev/null"]