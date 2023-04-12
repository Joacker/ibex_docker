# Get the GCC preinstalled image from Docker Hub
FROM ubuntu:18.04
# Copy the current folder which contains C++ source code to the Docker image under /usr/src
RUN apt update && apt install -y \
                        python2.7 \ 
                        flex \
                        bison \
                        gcc \
                        g++ \
                        make \
                        pkg-config\
                        curl \
                        cmake \
                        git \
                        python-pip

RUN git clone -b develop https://github.com/ibex-team/ibex-lib.git && cd ibex-lib && \
    mkdir build && cd build && \
    cmake -DCMAKE_CXX_FLAGS="-fPIC" -DCMAKE_C_FLAGS="-fPIC" .. && \
    make && make check && make install

RUN apt update

# RUN git clone https://github.com/benEnsta/pyIbex.git && cd pyIbex && \
#      git submodule update --init --recursive && \
#      mkdir -p build && cd build && \
#      make && make test && make pip_package && \
#      cd ./src/python_package && \
#      python ./setup.py develop

COPY . /usr/src/dockertest1

# Specify the working directory
WORKDIR /usr/src/dockertest1/app

# Use GCC to compile the Test.cpp source file
#RUN g++ -o Hola hola.cpp