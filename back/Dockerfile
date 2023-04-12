# Get the GCC preinstalled image from Docker Hub
FROM gcc:4.9

# Copy the current folder which contains C++ source code to the Docker image under /usr/src
COPY hola.cc /usr/src/dockertest1

# Specify the working directory
WORKDIR /usr/src/dockertest1/back

# Use GCC to compile the Test.cpp source file
#RUN g++ -o Hola hola.cpp