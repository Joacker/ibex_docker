FROM alpine:3.15


RUN apk update && apk add --no-cache \
    bash \
    g++ \
    gcc \
    flex \
    bison \
    python2 \
    make \
    wget \
    curl \
    openjdk8 

WORKDIR /app

COPY ./ibex-lib /app
RUN ./waf configure --lp-lib=soplex --interval-lib=gaol --lp-lib=soplex \
&& ./waf

# ./__build__/src/ibexopt benchs/optim/medium/ex14_2_7.bch --random-seed=1

# Mantener el contenedor en ejecución
CMD ["tail", "-f", "/dev/null"]