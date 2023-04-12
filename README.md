# ibex_docker

Si cambio cosas del algoritmo debo de hacer un ./waf install de nuevo

Para trabajar sobre un nuevo archivo de ejecución se debe de ejecutar el siguiente comando:
```sh
./__build__/src/ibexopt benchs/optim/medium/alkylbis.bch --random-seed=1
```
Al final de esa ruta hay que seleccionar el archivo que uno busca ejecutar dentro de los benchmarks.

Para levantar la topología, se tiene que emplear el siguiente comando:
```sh
docker-compose up --build -d
```

Luego para acceder al contenedor:
```sh
docker exec -it app bash
```