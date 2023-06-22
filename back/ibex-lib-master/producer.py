from kafka import KafkaProducer
from json import dumps
import time
import threading
import argparse
import random
import string

servidores_bootstrap = 'kafka:9092'
topic_hard = 'hard'
topic_medium = 'medium'
topic_easy = 'easy'


productor = KafkaProducer(bootstrap_servers=[servidores_bootstrap])

def generar_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 20)))

def enviar_temperatura():
    topic = topic_temperatura
    while True:
        temperatura = round(random.uniform(10, 30), 1)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "temperatura": temperatura
        }
        json_mensaje = dumps(mensaje).encode('utf-8')
        productor.send(topic, json_mensaje)
        print('Enviando JSON:', json_mensaje)
        time.sleep(3)

def enviar_porcentaje_humedad():
    topic = topic_humedad
    while True:
        humedad = random.randint(0, 100)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "porcentaje_humedad": humedad
        }
        json_mensaje = dumps(mensaje).encode('utf-8')
        productor.send(topic, json_mensaje)
        print('Enviando JSON:', json_mensaje)
        time.sleep(3)

def enviar_posicion():
    topic = topic_posicion
    while True:
        posicion = random.randint(0, 10)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "posicion": posicion
        }
        json_mensaje = dumps(mensaje).encode('utf-8')
        productor.send(topic, json_mensaje)
        print('Enviando JSON:', json_mensaje)
        time.sleep(3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="Número de hilos a crear")
    args = parser.parse_args()

    funciones_envio = [
        enviar_temperatura,
        enviar_porcentaje_humedad,
        enviar_posicion,
        enviar_color,
        enviar_peso
    ]

    threads = []
    for _ in range(args.num_threads):
        funcion_envio = random.choice(funciones_envio)
        t = threading.Thread(target=funcion_envio)
        t.start()
        threads.append(t)

    # Esperar a que todos los hilos finalicen
    for t in threads:
        t.join()